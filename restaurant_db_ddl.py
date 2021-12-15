from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

# create tables
class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, nullable=False)
    is_delivery = Column(Boolean, nullable=False)
    special_instructions = Column(String(200))
    chef_name = Column(String(50))
    # foreign key constraints
    table_num = Column(String(10), ForeignKey('dining_tables.table_num'), nullable=False)
    customer_name = Column(String(50), ForeignKey('customers.customer_name'), nullable=False)
    # cardinality
    order_items = relationship('OrderItems') # one-to-many with order items, parent=orders

class Customers(Base):
    __tablename__ = 'customers'
    customer_name = Column(String(50), primary_key=True, nullable=False)
    is_dining_in = Column(Boolean, nullable=False)
    phone_num = Column(String(12))
    # cardinality
    orders = relationship('Orders') # one-to-many with orders, parent=customers
    reservations = relationship('Reservations') # one-to-many with reservations, parent=customers

class OrderItems(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True, nullable=False)
    item_name = Column(String(50), nullable=False)
    quantity = Column(Integer, nullable=False)
    is_vegeterian = Column(Boolean, nullable=False)
    price = Column(Numeric(10,2), nullable=False)
    # foreign key constraint
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)

class Reservations(Base):
    __tablename__ = 'reservations'
    id = Column(Integer, primary_key=True, nullable=False)
    num_guests = Column(Integer, nullable=False)
    date_time = Column(String(50), nullable=False)
    # foreign key constraint
    customer_name = Column(String(50), ForeignKey('customers.customer_name'), nullable=False) # one-to-many with customers, parent=customers

class DiningTables(Base):
    __tablename__ = 'dining_tables'
    table_num = Column(String(10), primary_key=True, nullable=False)
    table_type = Column(String(20), nullable=False)
    capacity = Column(Integer, nullable=False)
    server_name = Column(String(50))
    # cardinality
    table_status = relationship('TableStatus', back_populates='dining_tables', uselist=False) # one-to-one with table status, parent=dining tables
    orders = relationship('Orders') # one-to-many with orders, parent=dining tables

class TableStatus(Base):
    __tablename__ = 'table_status'
    id = Column(Integer, primary_key=True, nullable=False)
    status = Column(String(20), nullable=False)
    dine_in_time = Column(String(50), nullable=False)
    dine_out_time = Column(String(50), nullable=False)
    num_guests = Column(Integer, nullable=False)
    # foreign key constraint
    table_num = Column(String(4), ForeignKey('dining_tables.table_num'), nullable=False)
    # cardinality
    dining_tables = relationship('DiningTables', foreign_keys=[table_num], back_populates='table_status') # one-to-one with dining tables, parent=dining tables

# to create database file
engine = create_engine('sqlite:///restaurant.db', echo=True)
Base.metadata.create_all(engine)

