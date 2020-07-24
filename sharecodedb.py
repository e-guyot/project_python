#!/usr/bin/env python3

from datetime import datetime

from socket import socket

import os

from flask import Flask, request, render_template, \
                  redirect

from model_sqlite import get_last_code_bdd, \
                         save_bdd, \
                         get_code, \
                         get_lang, \
                         update_code

from model_sqlite_users import save_user

app = Flask(__name__)


@app.route('/')
def index():
    #d = { 'last_added':[ { 'uid':'testuid', 'code':'testcode' } ] }
    d = { 'last_added':get_last_code_bdd() }
    return render_template('index.html',**d)

@app.route('/create')
def create():
    uid = save_bdd()
    return redirect("{}edit/{}".format(request.host_url,uid))
    
@app.route('/edit/<string:uid>/')
def edit(uid):
    code = get_code(uid)
    lang = get_lang(uid)
    # current date and time
    date = datetime.now()
    ip = os.system('hostname -i')
    navigateur = request.headers.get('User-Agent')

    user = save_user(ip, navigateur, date)
    if code is None:
        return render_template('error.html',uid=uid)
    d = dict( uid=uid, code=code, lang=lang,
              url="{}view/{}".format(request.host_url,uid))
    return render_template('edit.html', **d) 

@app.route('/publish',methods=['POST'])
def publish():
    code = request.form['code']
    uid  = request.form['uid']
    lang = request.form['lang']
    update_code(uid,code,lang)
    return redirect("{}{}/{}".format(request.host_url,
                                     request.form['submit'],
                                     uid))

@app.route('/view/<string:uid>/')
def view(uid):
    code = get_code(uid)
    if code is None:
        return render_template('error.html',uid=uid)
    d = dict( uid=uid, code=code,
              url="{}view/{}".format(request.host_url,uid))
    return render_template('view.html', **d)

@app.route('/admin/')
def admin():
    user= totoip
    return render_template('admin.html’, user)

if __name__ == '__main__':
    app.run()

