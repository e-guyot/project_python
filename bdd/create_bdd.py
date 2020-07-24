from sqlite3 import *

# create bdd codes 

conn = connect("bdd/tab_codes.db")
cur = conn.cursor()
cur.execute("CREATE TABLE codes (id VARCHAR(20) PRIMARY KEY NOT NULL, code TEXT NOT NULL, lang TEXT)")
conn.commit()
cur.close()
conn.close()


# create bdd users

conn = connect("bdd/tab_users.db")
cur = conn.cursor()
cur.execute("CREATE TABLE users (id_user INTEGER PRIMARY KEY AUTOINCREMENT, ip_adress VARCHAR(20) NOT NULL, naviguateur text, date TIMESTAMP)") 
conn.commit()
cur.close()
conn.close()