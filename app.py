# Programmed By : Suman Gangopadhyay
# Email ID : linuxgurusuman@gmail.com
# Date : 15-May-2018
# Language : Python3.6
# Framework : Flask
# Copyright © 2018 Suman Gangopadhyay

from flask import Flask
from flask import redirect
from flask import url_for
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import pymysql
import os

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    db = pymysql.connect("localhost","root","suman","flask_blog")
    cur = db.cursor()
    if (cur):
        sql = """SELECT * FROM new_users """
        cur.execute(sql)
        res = cur.fetchall()
        sl_no = 0
        for rows in res:
            sl_no = sl_no + 1
    else:
        return "EERROR : Unable to connect to Database"
    return "Number of Data : {}".format(sl_no)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
