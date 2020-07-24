#!/usr/bin/env python3

from model import create_uid

from sqlite3 import *

def get_last_code_bdd():
    conn = connect("bdd/tab_codes.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM codes")
    d = cur.fetchall()
    cur.close()
    conn.close()
    return d

def save_bdd():
    uid = create_uid()
    conn = connect("bdd/tab_codes.db")
    cur = conn.cursor()
    code = '# Write your code here...'
    lang = ''
    cur.execute('INSERT INTO codes(id, code,lang) VALUES(?,?,?)', (uid, code, lang))
    conn.commit()
    cur.close()
    conn.close()
    return uid

def get_code(uid):
    conn = connect("bdd/tab_codes.db")
    cur = conn.cursor()
    cur.execute("SELECT code FROM codes where id = '"+uid+"'")
    d = cur.fetchone()
    cur.close()
    conn.close()
    return d[0]

def get_lang(uid):
    conn = connect("bdd/tab_codes.db")
    cur = conn.cursor()
    cur.execute("SELECT lang FROM codes where id = '"+uid+"'")
    d = cur.fetchone()
    cur.close()
    conn.close()
    return d[0]

def update_code(uid=None,code=None,lang=None):
    if uid is None:
        uid = create_uid()
        code = '# Write your lang here...'
        lang = ''
    conn = connect("bdd/tab_codes.db")
    cur = conn.cursor()
    print(code)
    cur.execute("UPDATE codes SET code = '"+code+"', lang = '"+lang+"' where id = '"+uid+"'")
    conn.commit()
    cur.close()
    conn.close()
    return uid


print(get_last_code_bdd())