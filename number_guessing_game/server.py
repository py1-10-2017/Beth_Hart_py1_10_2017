from flask import Flask, render_template, redirect, session, request
import random
app = Flask(__name__)
app.secret_key ="going west"


@app.route('/', methods=["get", "post"])
def home():
 
    session['num'] = random.randrange(1, 101)
    print session['num']
    return render_template("index.html")

@app.route('/guess', methods=["post", "get"])
def guess():
    guess = int(request.form['guess'])
    # print type(session["num"]) //ERROR as to why msg did not print
    # print type(guess)
    if guess == session['num']:
        msg = "you guessed it!"
    elif guess > session['num']:
        msg = "your guess is too high"
    elif guess < session['num']:
        msg = " your guess is too low"
    print msg
    return render_template("index.html", msg=msg)



app.run(host="0.0.0.0", port=int("8080"), debug=True)
