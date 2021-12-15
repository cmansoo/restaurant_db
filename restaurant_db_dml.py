from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from restaurant_db_ddl import Orders, OrderItems, Customers, Reservations, DiningTables, TableStatus

engine = create_engine('sqlite:///restaurant.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# crate data
customer_1 = Customers(customer_name='Mansoo Cho', is_dining_in=True, phone_num='123-456-7890')
customer_2 = Customers(customer_name='James Hanson', is_dining_in=False, phone_num='098-765-4321')

order_1 = Orders(id=1, is_delivery=False, special_instructions=None, chef_name='Ray Hernandez', table_num='K1', customer_name='Mansoo Cho')
order_2 = Orders(id=2, is_delivery=True, special_instructions='Please include utensils', chef_name='Ray Hernandez', table_num='delivery', customer_name='James Hanson')

order_items_1 = OrderItems(id=1, item_name='seafood pasta', quantity=1, is_vegeterian=False, price=10.00, order_id=1)
order_items_2 = OrderItems(id=2, item_name='bread sticks', quantity=2, is_vegeterian=True, price=7.00, order_id=1)
order_items_3 = OrderItems(id=3, item_name='pepperoni pizza(L)', quantity=1, is_vegeterian=False, price=14.00, order_id=2)
order_items_4 = OrderItems(id=4, item_name='cheese pasta', quantity=1, is_vegeterian=True, price=8, order_id=2)

reservation_1 = Reservations(id=1, num_guests=2, date_time='2021-12-14 18:00:00', customer_name='Mansoo Cho')

dining_table_1 = DiningTables(table_num='K1', table_type='indoor', capacity=6, server_name='Kim Smith')
dining_table_2 = DiningTables(table_num='delivery', table_type='delivery', capacity=0, server_name=None)

table_status_1 = TableStatus(id=1, status='occupied', dine_in_time='2021-12-14 18:00:00', dine_out_time='2021-12-14 19:00:00', num_guests=2, table_num='K1')
table_status_2 = TableStatus(id=2, status='delivered', dine_in_time='2021-12-14 16:00:00', dine_out_time='2021-12-14 16:15:00', num_guests=0, table_num='delivery')

# insert data
session.add_all([customer_1, customer_2, order_1, order_2, order_items_1, order_items_2, order_items_3, order_items_4, reservation_1, dining_table_1, dining_table_2, table_status_1, table_status_2])
session.commit()


