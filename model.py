from datetime import datetime,timezone
from database import base
from sqlalchemy import Column,String,DateTime,Boolean,Float,Integer,ForeignKey,Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

class MenuItem(base):
    __tablename__ = "menuitems"
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    name = Column(String)
    category = Column(String)
    price = Column(Float)
    description = Column(String)
    is_available = Column(Boolean,default=True)


class Conversation(base):
    __tablename__ = "conversations"
    id = Column(UUID(as_uuid=True),primary_key=True,default = uuid.uuid4)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))


class Message(base):
    __tablename__ = "messages"
    id = Column(UUID(as_uuid=True),primary_key=True,default = uuid.uuid4)
    conversation_id = Column(UUID(as_uuid=True),ForeignKey("conversations.id"))
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    content = Column(Text)
    role = Column(String)


class Table(base):
    __tablename__ = "tables"
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    table_number = Column(Integer)
    capacity = Column(Integer)


class Booking(base):
    __tablename__ = "bookings"
    id = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4)
    customer_name = Column(String)
    customer_phone = Column(String)
    party_size = Column(Integer)
    table_id = Column(UUID(as_uuid=True),ForeignKey("tables.id"))
    booking_time = Column(DateTime)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    status = Column(String,default="confirmed")