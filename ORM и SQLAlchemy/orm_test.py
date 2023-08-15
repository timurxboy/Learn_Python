# import sqlalchemy
# from sqlalchemy import text
#
# print(sqlalchemy.__version__)
#
# engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:adminadmin@localhost:5432/testdb')
#
# connection = engine.connect()
#
# stmt = text("SELECT * FROM book")
# result = connection.execute(stmt)
# for row in result:
#     print('title',)
#
# result.close()
#
#
# trans = connection.begin()
# try:
#     connection.execute("INSERT INTO book(book_id, title, isbn, publisher_id, weight) VALUES (32, 'worst book', 12345, 2, 10)")
#     trans.commit()
# except:
#     trans.rollback()
#     raise
#
# with connection.begin() as trans:
#     connection.execute("INSERT INTO book(book_id, title, isbn, publisher_id, weight) VALUES (32, 'best book', 12345, 1, 10)")
#
# stmt = text("SELECT * FROM book")
# result = connection.execute(stmt)
# for row in result:
#     print('title',)
#
# result.close()

import sqlalchemy

engine = sqlalchemy.create_engine("postgresql+psycopg2://postgres:adminadmin@localhost:5432/testdb")
engine.connect()

print(engine)