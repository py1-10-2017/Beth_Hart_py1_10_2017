from flask import Flask, session, redirect, render_template, flash, request

from mysqlconnection import MySQLConnection
app = Flask(__name__)
mysql = MySQLConnection(app, "full_friends")

app.secret_key = "easy to ignore"

@app.route('/')
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template("index.html", friends=friends)
    
@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, email, created_at) VALUES(:first_name, :last_name, :email, now())"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    mysql.query_db(query, data)
    return redirect('/')
    
@app.route('/friends/<id>/edit')
def edit(id):
    query = "SELECT * FROM friends where id=:id"
    data = {'id':id}
    friend = mysql.query_db(query,data)
    return render_template("edit.html", friend=friend)
    
@app.route('/friends/<id>', methods=['POST'])
def update(id):
    query = "UPDATE friends SET first_name=:first_name, last_name=:last_name, email=:email, created_at= now() WHERE id=:id"
    data ={
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'], 
        'id': id
    }
    mysql.query_db(query, data)
    return redirect('/')
    
@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    query = "DELETE FROM friends where id=:id"
    mysql.query_db(query, {'id':id})
    return redirect("/")
    

app.run(host="0.0.0.0", port=int("8080"), debug=True)
