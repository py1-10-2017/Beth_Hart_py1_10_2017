from flask import Flask, session, redirect, render_template, flash, request
import re
from mysqlconnection import MySQLConnection
from time import strptime, strftime

app = Flask(__name__)
mysql = MySQLConnection(app, "email_val")
regex_obj = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app.secret_key = "slowly slowly catchy monkey"

@app.route('/')
def new():
    #show form
    return render_template('index.html')
    
@app.route('/create', methods=["POST"])
def create():
    if not regex_obj.match(request.form['email']):
        flash("Please enter a valid email address.")
        return redirect('/')
    else:
        flash("The email address you entered is valid! Thank you!")
        query = "INSERT INTO emails(email, created_at, updated_at) VALUES (:email, now(), now())";
        mysql.query_db(query, {'email':request.form['email']})    
        return redirect("/show")
    
    
@app.route("/show")
def show():
    query = "SELECT email, created_at FROM emails";
    all_emails = mysql.query_db(query)
    print all_emails
    return render_template('show.html', emails=all_emails)

app.run(host="0.0.0.0", port=int("8080"))
