from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

from restaurant_db_ddl import Orders, OrderItems, Customers, Reservations, DiningTables, TableStatus

engine = create_engine('sqlite:///restaurant.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# run queries
for row in session.query(Customers).all():
    print(row.customer_name, row.is_dining_in, row.phone_num)

for row in session.query(Customers).order_by(Customers.customer_name):
    print(row.customer_name, row.is_dining_in, row.phone_num)

# using where clause
for row in session.query(Customers).filter(Customers.customer_name=='Mansoo Cho'):
    print(row.customer_name, row.is_dining_in, row.phone_num)

# queries with joins
for c, r in session.query(Customers, Reservations).filter(Customers.customer_name==Reservations.customer_name).filter(Customers.customer_name=='Mansoo Cho').all():
    print(c.customer_name, c.is_dining_in, c.phone_num, r.id, r.num_guests, r.date_time)

# use count function
print(session.query(func.count('*')).select_from(OrderItems).scalar())