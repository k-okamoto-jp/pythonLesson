import sqlite3

conn = sqlite3.connect('test_sqlite.db')

curs = conn.cursor()

# curs.execute(
#     'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
# conn.commit()

# curs.execute(
#     'INSERT INTO persons(name) values("RIHO")'
# )
# conn.commit()

curs.execute('UPDATE persons set name = "Michel" WHERE name = "MIKE"')
conn.commit()

curs.execute('DELETE FROM persons WHERE name = "Michel"')
conn.commit()

curs.execute(
    'SELECT * from persons'
)
print(curs.fetchall())

curs.close()
conn.close()