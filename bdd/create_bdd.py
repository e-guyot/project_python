from sqlite3 import *

# create bdd codes 

conn = connect("bdd/tab_codes.db")
cur = conn.cursor()
cur.execute("CREATE TABLE code (id VARCHAR(20) PRIMARY KEY NOT NULL, code TEXT NOT NULL, lang TEXT)")
conn.commit()
cur.close()
conn.close()


# create bdd users

conn = connect("bdd/tab_users.db")
cur = conn.cursor()
cur.execute("CREATE TABLE users (id VARCHAR(20) PRIMARY KEY NOT NULL, ip_adress TEXT NOT NULL, naviguateur text, date TIMESTAMP)") 
conn.commit()
cur.close()
conn.close()