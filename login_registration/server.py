from flask import Flask, session, render_template, request, redirect, flash
from mysqlconnection import MySQLConnection
from flask_bcrypt import Bcrypt
import re


app = Flask(__name__)
app.secret_key = "i know sam hill"
mysql = MySQLConnection(app, 'login_registration')
bcrypt= Bcrypt(app)
regex_obj = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/user/login', methods=['POST'])
def login():
    email = request.form["email"]
    query = 'SELECT * FROM users WHERE email=:email LIMIT 1'
    data = {'email': email}
    user = mysql.query_db(query, data)
    password =request.form['password']
    if user:
        if bcrypt.check_password_hash(user[0]['password'],password):
            session['id'] = user[0]['id']
            print session['id']
            flash("Welcome back, {}".format(user[0]["first_name"] + "!"))
            return redirect('/dogs')
        else:
            flash('Wrong password. Please try again')
            return redirect('/')
    else:
        flash("Email address not found. Please try a different address or register if you are a new user.")
        return redirect('/')
# =====================
# register
# =====================

@app.route('/user/new')
def new():
    return render_template("register.html")


@app.route('/user', methods=['POST'])
def create():
    password = request.form['password']
    valid = True
    if len(request.form['first_name']) < 2 or len(request.form['last_name']) < 2 or not request.form['first_name'].isalpha() or not request.form['last_name'].isalpha():
        flash("Invalid name. First and last name must be letters only and at least 2 characters long.")
        valid = False
    if len(password)< 8:
        flash('Invalid password. Password must be at least 8 characters.')
        valid = False
    if not regex_obj.match(request.form['email']):
        flash("Invalid email. Enter a valid email address.")
        valid = False
    if valid == True:
        hashed_pw = bcrypt.generate_password_hash(password)
        query = "INSERT INTO users (first_name, last_name, email, password, created_at) VALUES(:first_name,:last_name,:email, :password, now());"
        data= {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': hashed_pw
        }
        mysql.query_db(query, data)
        get_id= mysql.query_db("SELECT id from users where email=:email", data)
        session["id"] = get_id[0]
        print session['id']
        return redirect('/dogs')
    else:
        return redirect('/user/new')

@app.route('/dogs', methods=["GET"])
def show():
    try:
        if session["id"]:
            return render_template('show.html')
    except:
        return redirect('/')




app.run(host='0.0.0.0', port=int('8080'), debug=True)