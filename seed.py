from database import SessionLocal
from model import MenuItem,Table

def seed():
    db = SessionLocal()
    try:
        if db.query(MenuItem).first():
            print("already seeded")
            return
        print("seed file started")
        menu_items = [
            MenuItem(name="Buffalo Wings", category="Appetizers", price=12.99,
                     description="Crispy chicken wings tossed in spicy buffalo sauce, served with ranch"),
            MenuItem(name="Calamari Fritti", category="Appetizers", price=14.50,
                     description="Lightly breaded calamari with lemon aioli"),
            MenuItem(name="Caesar Salad", category="Appetizers", price=10.99,
                     description="Romaine, parmesan, garlic croutons, classic Caesar dressing"),
            MenuItem(name="Clam Chowder", category="Appetizers", price=9.99,
                     description="Creamy New England style chowder in a sourdough bowl"),
            MenuItem(name="Loaded Nachos", category="Appetizers", price=13.50,
                     description="Tortilla chips with cheddar, jalapenos, sour cream and guacamole"),

            MenuItem(name="Classic Cheeseburger", category="Mains", price=16.99,
                     description="Angus beef patty, cheddar, lettuce, tomato, brioche bun, fries"),
            MenuItem(name="Grilled Salmon", category="Mains", price=26.99,
                     description="Atlantic salmon with lemon butter, asparagus and mashed potatoes"),
            MenuItem(name="Ribeye Steak", category="Mains", price=38.99, is_available=False,
                     description="12oz ribeye grilled to order with garlic herb butter and roasted vegetables"),
            MenuItem(name="Chicken Alfredo", category="Mains", price=21.50,
                     description="Fettuccine in creamy parmesan sauce with grilled chicken"),
            MenuItem(name="Fish Tacos", category="Mains", price=17.99,
                     description="Grilled white fish, cabbage slaw, chipotle crema, three corn tortillas"),
            MenuItem(name="Margherita Pizza", category="Mains", price=18.00,
                     description="Fresh mozzarella, basil, tomato sauce, wood-fired crust"),
            MenuItem(name="Veggie Burger", category="Mains", price=15.99,
                     description="Plant-based patty with avocado, lettuce, tomato (vegetarian)"),

            MenuItem(name="New York Cheesecake", category="Desserts", price=9.50,
                     description="Creamy cheesecake with strawberry compote"),
            MenuItem(name="Chocolate Lava Cake", category="Desserts", price=10.50,
                     description="Warm chocolate cake with a molten center, vanilla ice cream"),
            MenuItem(name="Apple Pie", category="Desserts", price=8.99, is_available=False,
                     description="Warm cinnamon apple pie with a scoop of vanilla ice cream"),

            MenuItem(name="Fresh Lemonade", category="Drinks", price=4.50,
                     description="House-made lemonade with mint"),
            MenuItem(name="Iced Tea", category="Drinks", price=3.50,
                     description="Freshly brewed, sweetened or unsweetened"),
            MenuItem(name="Craft Root Beer", category="Drinks", price=5.00,
                     description="Local San Diego craft root beer"),
        ]

        table_data = [
            (1, 2), (2, 2), (3, 2), (4, 2),
            (5, 4), (6, 4), (7, 4),
            (8, 6), (9, 6),
            (10, 8),
        ]
        tables = [Table(table_number=n, capacity=c) for n, c in table_data]

        db.add_all(menu_items)
        db.add_all(tables)
        db.commit()
        print("seeded!")

    finally:
        db.close()

if __name__ == "__main__":
    seed()