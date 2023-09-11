import sqlalchemy
from sqlalchemy.orm import sessionmaker

from hw_db_task5_models import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = 'postgresql://postgres:Ksenya240197@localhost:5432/hw_db_task5'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()


# pu = Publisher(name='Пушкин')

# b1 = Book(title='Капитанская дочка', publisher=pu)
# b2 = Book(title='Руслан и Людмила', publisher=pu)
# b3 = Book(title='Евгений Онегин', publisher=pu)

# sh1 = Shop(name='Буквоед')
# sh2 = Shop(name='Лабиринт')
# sh3 = Shop(name='Книжный дом')

# st1 = Stock(count=10, book=b1, shop=sh1)
# st2 = Stock(count=12, book=b2, shop=sh1)
# st3 = Stock(count=9, book=b1, shop=sh2)
# st4 = Stock(count=5, book=b3, shop=sh3)

# Sale1 = Sale(price=600, date_sale='09-11-2022', count=1, stock=st1)
# Sale2 = Sale(price=500, date_sale='08-11-2022', count=1, stock=st2)
# Sale3 = Sale(price=580, date_sale='05-11-2022', count=1, stock=st3)
# Sale4 = Sale(price=490, date_sale='02-11-2022', count=1, stock=st4)
# Sale5 = Sale(price=600, date_sale='26-10-2022', count=1, stock=st1)

# session.add(pu)
# session.add_all([b1, b2, b3])
# session.add_all([sh1, sh2, sh3])
# session.add_all([st1, st2, st3, st4])
# session.add_all([Sale1, Sale2, Sale3, Sale4, Sale5])
# session.commit()


subq1 = session.query(Stock).join(Sale, Stock.id == Sale.id_stock)
subq2 = session.query(Shop).join(subq1, Shop.id == subq1.c.id_shop)
subq3 = session.query(Book).join(subq2, Book.id == subq2.c.id_book)
q = session.query(Publisher).join(subq3, Publisher.id == subq3.c.id_publisher)
# print(q)
for s in q.all():
    if Publisher.name == input():
        print(s.title, s.name, s.price, s.date_sale)
    else:
        print('None')


session.close()
