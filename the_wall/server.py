from flask import Flask, session, redirect, render_template, flash, request
from mysqlconnection import MySQLConnection
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
mysql = MySQLConnection(app, "wall")
app.secret_key = "fetch kk, good gurl"
bcyrpt = Bcrypt(app)
regex_obj = re.compile(u'pattern)

app.run(host"0.0.0.0", port=int('8080'), debug=True)