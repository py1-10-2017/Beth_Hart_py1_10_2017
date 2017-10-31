from flask import Flask, session, redirect, render_template, flash, request
from mysqlconnection import MySQLConnection
from flask_bcrypt import Bcrypt
import re
import datetime

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
            return redirect('/messages')
        else:
            flash("Your password does not match our records. Please try again.", "danger")
            return redirect('/')
    else:
        flash("Email not found. If you have not registered please sign up.")


@app.route('/users/register', methods=['POST'])
def register():
    password = request.form['password']
    valid = True
    if len(request.form['first_name']) < 2 or len(request.form['last_name']) < 2:
        flash("Invalid name. First and last name are required and must be at least 2 characters long.", "danger")
        valid=False
    if not regex_obj.match(request.form['email']):
        flash("Email address is not valid. Enter email in correct format.")
        valid=False
    if len(request.form['password'])< 8:
        flash('Password must be at least 8 characters long.', 'danger')
        valid=False
    if request.form['password'] != request.form['conf_pw']:
        flash('Passwords do not match.', 'danger')
        valid=False
    if valid == False:
        return redirect('/')
    else:
        pw_hash = bcrypt.generate_password_hash(password)
        query = "INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) VALUES(:first_name, :last_name, :email, :password, NOW(), NOW())"
        data = {'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': pw_hash}
        mysql.query_db(query, data)
        get_id = mysql.query_db("SELECT id from users WHERE email=:email", data)
        session['id'] = get_id[0]['id']
        flash("Welcome, {}".format(request.form['first_name']), 'success')
        return redirect('/messages')

@app.route('/messages')
def home():
    msg_query = "SELECT users.id as uid, message, first_name, last_name, messages.created_at, messages.id as id, timestampdiff(minute, messages.created_at, now()) as timediff FROM  users JOIN messages on users.id=messages.user_id"
    user_messages = mysql.query_db(msg_query)
    print user_messages
    comment_query = "SELECT users.id, comment, message_id, first_name, last_name, comments.created_at FROM comments JOIN users on user_id=users.id order by comments.created_at desc"
    comments= mysql.query_db(comment_query)
    print session['id']
    
    return render_template('wall.html', user_messages = user_messages, comments=comments)
    
@app.route('/messages', methods=['POST'])
def new_message():
    print session['id']
    query = "INSERT INTO messages(user_id, message, created_at, updated_at) VALUES(:user_id, :message, now(), now())"
    data = {'user_id': session['id'],
            'message': request.form['message']
            }
    mysql.query_db(query, data)
    return redirect('/messages')
    
@app.route('/messages/<msg_id>/comments', methods=['POST'])
def new_comment(msg_id):
    query = "INSERT INTO comments(user_id, message_id, comment, created_at, updated_at) VALUES(:user_id, :message_id, :comment, now(), now())"
    data = {'user_id': session['id'],
            'message_id': msg_id,
            'comment': request.form['comment']
            }
    mysql.query_db(query, data)
    return redirect('/messages')  
    
@app.route('/messages/<msg_id>/delete')
def detroy(msg_id):
    query = "DELETE FROM messages WHERE :msg_id = id"
    data = {"msg_id": msg_id}
    mysql.query_db(query, data)
    return redirect('/messages')
app.run(host="0.0.0.0", port=int('8080'), debug=True)