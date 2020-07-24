from sqlite3 import *

# tab_users 

def save_user(ip_adress, naviguateur, date):
    conn = connect("bdd/tab_users.db")
    cur = conn.cursor()
    cur.execute('INSERT INTO users(ip_adress,naviguateur, date) VALUES(?,?,?)', (ip_adress, naviguateur, date))
    conn.commit()
    cur.close()
    conn.close()
    return True

def get_all_users():
    conn = connect("bdd/tab_users.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    d = cur.fetchall()
    cur.close()
    conn.close()
    return d

def get_ip_users():
    conn = connect("bdd/tab_users.db")
    cur = conn.cursor()
    cur.execute("SELECT ip_adress FROM users")
    d = cur.fetchall()
    cur.close()
    conn.close()
    return d[0]