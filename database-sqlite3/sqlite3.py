
# sqlite3 with python

import sqlite3

conn = sqlite3.connect('my_app.db')

# get the cursor
cur = conn.cursor()

# Create table products using cursor
cur.execute('CREATE TABLE products(name, price, quantity)')
res = curr.execute('select name from sqlite_master')
res.fetchone()
('products',)

# inserting multiple data items to products table
cur.execute("""
 insert into products values('Bag', 12.50, 25),('Laptop', 1240, 50);
 """)
 
# select from products
res = cur.execute("select name, price, num_of_stocks from products");
res.fetchall()


#------

# parametaraized queries to avoid sql injection attacks

cur.executemany("insert into products  values(?,?,?)", data)
conn.commit()
for row in cur.execute("select * from products order by price"):
    print(row)

('Bag', 12.5, 25)
('Earphone', 20.22, 50)
('Shirt-Z', 25.52, 12)
('Pant-Z', 34.23, 33)
('Laptop', 1240, 50)

conn.close()

#----

# dumping database with iterdump
conn = sqlite3.connect('tutorial.db')
with open('tutorial.sql', 'w') as f:
    for line in conn.iterdump():
        f.write('%s\n' % line)


conn.close()

#------

# connection with context maanger sqlite3

conn = sqlite3.connect('tutorial.db')
try:
    with conn:
        conn.execute("insert into products(name, price, num_of_stocks) values('P4', 22.33, 234)")
        time.sleep(50)
        conn.execute("insert into products(name, price, num_of_stocks) values('P5', 22.33, 234)")
except sqlite3.IntegrityError:
    print('something wrong')

#----


#adapter and converter



class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Coordinates({self.x}, {self.y})"
      

def adapt_coord(coordinates):
    return f"{coordinates.x};{coordinates.y}"

def convert_coord(s):
    x, y = list(map(float, s.split(b";")))
    return Coordinate(x, y)


sqlite3.register_adapter(Coordinates, adapt_coord)
sqlite3.register_converter(Coordinates, convert_coord)

c = Coordinates(22.2323, 34.2323)

conn = sqlite3.connect('tutorial.db', detect_types=sqlite3.PARSE_DECLTYPES)
cur = conn.cursor()
cur.execute("create table test3(c Coordinates)")
res = cur.execute("insert into test3(c) values(?)", (c,))
res.fetchall()


