from flask import Flask, session, redirect, render_template, flash, request
from mysqlconnection import MySQLConnection
from flask_bcrypt import Bcrypt
import re


app = Flask(__name__)
app.secret_key = "fetch kk, good gurl"
mysql = MySQLConnection(app, "wall")
bcrypt = Bcrypt(app)

regex_obj = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    return render_template('index.html')
    
    
@app.route('/users/login', methods=['POST'])
def login():
    password = request.form['password']
    query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    data = {"email" : request.form["email"]}
    user = mysql.query_db(query,data)
    if user:
        if bcrypt.check_password_hash(user[0]['password'], password):
            session['id']= user[0]['id']
            return redirect('/wall')
        else:
            flash("Your password does not match our records. Please try again.", "danger")
            return redirect('/')
    else:
        flash("Email not found. If you are a new user, please register.", "danger")

@app.route('/users/register', methods=['POST'])
def register():
    #validate form input
    #encrypt password
    password = request.form['password']
    pw_hash = bcrypt.generate_password_hash(password)
    #add information to DB
    query = "INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) VALUES(:first_name, :last_name, :email, :password, NOW(), NOW())"
    data = {'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'email': request.form['email'],
    'password': pw_hash}
    mysql.query_db(query, data)
    get_id = mysql.query_db("SELECT id from users WHERE email=:email", data)
    
    session['id'] = get_id[0]['id']
    print session['id']
    flash("Welcome, {}".format(request.form['first_name']), 'success')
    return redirect('/wall')

@app.route('/wall')
def home():
    msg_query = "SELECT message, first_name, last_name, messages.created_at, messages.id as id FROM  users JOIN messages on users.id=messages.user_id"
    user_messages = mysql.query_db(msg_query)
    print user_messages
    comment_query = "SELECT comment, message_id, first_name, last_name, comments.created_at FROM comments JOIN users on user_id=users.id order by comments.created_at desc"
    comments= mysql.query_db(comment_query)
    print comments
    return render_template('wall.html', user_messages = user_messages, comments=comments)
    
@app.route('/messages', methods=['POST'])
def new_message():
    print session['id']
    query = "INSERT INTO messages(user_id, message, created_at, updated_at) VALUES(:user_id, :message, now(), now())"
    data = {'user_id': session['id'],
            'message': request.form['message']
            }
    mysql.query_db(query, data)
    return redirect('/wall')
    
@app.route('/messages/<msg_id>/comments', methods=['POST'])
def new_comment(msg_id):
    query = "INSERT INTO comments(user_id, message_id, comment, created_at, updated_at) VALUES(:user_id, :message_id, :comment, now(), now())"
    data = {'user_id': session['id'],
            'message_id': msg_id,
            'comment': request.form['comment']
            }
    mysql.query_db(query, data)
    return redirect('/wall')  
app.run(host="0.0.0.0", port=int('8080'), debug=True)