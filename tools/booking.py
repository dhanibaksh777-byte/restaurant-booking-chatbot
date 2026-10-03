from datetime import datetime,timedelta
from model import Table,Booking


def check_availablity(db,party_size,date_time):
    requested_time = datetime.fromisoformat(date_time)
    window_start = requested_time - timedelta(minutes=90)
    window_end = requested_time + timedelta(minutes=90)

    customer_table = db.query(Table).filter(Table.capacity >= party_size).all()

    for table in customer_table:
        clash = db.query(Booking).filter(Booking.table_id == table.id,Booking.status == "confirmed",Booking.booking_time.between(window_start,window_end)).first()
        if clash is None:
            return table
    return None

def create_booking(db,customer_name,customer_phone,party_size,date_time,table_id):
    booking_time = datetime.fromisoformat(date_time)
    new_booking = Booking(customer_name = customer_name,customer_phone = customer_phone,party_size = party_size,table_id = table_id,booking_time = booking_time)
    db.add(new_booking)
    db.commit()
    return {"status": "confirmed", "table_id": table_id, "booking_time": date_time}

def book_table(db,customer_name,customer_phone,party_size,date_time):
    table = check_availablity(db,party_size,date_time)
    if table is None:
        return {"status": "unavailable", "message": "No tables available at that time."}
    return create_booking(db, customer_name, customer_phone, party_size, date_time, table.id)


book_table_tool = {
    "type": "function",
    "function": {
        "name": "book_table",
        "description": "Book a table for a customer. Checks availability and creates the booking if a table is free.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_name": {
                    "type": "string",
                    "description": "Full name of the customer making the booking."
                },
                "customer_phone": {
                    "type": "string",
                    "description": "Customer's contact phone number."
                },
                "party_size": {
                    "type": "integer",
                    "description": "Number of people in the party."
                },
                "date_time": {
                    "type": "string",
                    "description": "Requested date and time in ISO 8601 format, e.g. 2026-10-05T20:00:00"
                }
            },
            "required": ["customer_name", "customer_phone", "party_size", "date_time"]
        }
    }
}