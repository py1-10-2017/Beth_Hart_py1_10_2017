from flask import Flask, render_template, redirect, session, request, flash
import random
app = Flask(__name__)
app.secret_key ="going west"


@app.route('/', methods=["get", "post"])
def home():
    if "num" not in session:
        session['num'] = random.randrange(1, 101)
    print session['num']
    return render_template("index.html")

@app.route('/guess', methods=["post", "get"])
def guess():
    if not request.form['guess'].isdigit():
        flash("invalid entry -- enter only numbers")
        return redirect('/')
    guess = int(request.form['guess'])
    # print type(session["num"]) //ERROR as to why msg did not print
    # print type(guess)
    if guess == session['num']:
        session["msg"] = "you guessed it!"
    elif guess > session['num']:
        session["msg"] = "your guess is too high"
    elif guess < session['num']:
        session["msg"] = " your guess is too low"
    return redirect("/")

@app.route('/reset')
def play_again():
    session.clear()
    return redirect('/')


app.run(host="0.0.0.0", port=int("8080"), debug=True)
