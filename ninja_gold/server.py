from flask import Flask, render_template, redirect, session, request
import random
from time import gmtime, strftime

app = Flask(__name__)

app.secret_key = "just do it"


@app.route('/', methods=["get"])
def ninja():
    if "total" in session:
        session["total"]= session["total"]
    else:
        session["total"] = 0
    return render_template("index.html", session=session)
    
@app.route("/process_money", methods=["post"])
def gold():
    time = str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    print time
    action = request.form['action']
    print action
    
    if action == "farm":
        num = random.randrange(10, 21)
        session['total'] += num
        new = "Congrats! You have earned "+ str(num) + " golds!  (" + time + ")"
    elif action == "cave":
        num = random.randrange(5, 11)
        session['total'] += num
        new = "Congrats! You have earned "+ str(num) + " golds!  (" + time + ")"
    elif action == "house":
        num = random.randrange(2, 5)
        session['total'] += num
        new = "Congrats! You have earned "+ str(num) + " golds!  (" + time + ")"
    elif action == "casino":
        num = random.randrange(10, 51)
        if num % 2 == 0:
            session["total"] -= num
            new = "Oh no! You lost "+ str(num) + " golds!  (" + time + ")"
        else:
            session["total"] += num
            new = "Congrats! You have earned "+ str(num) + " golds!  (" + time + ")"
    if "msg" in session:
        session['msg'].insert(0,new)
    else:
        session['msg'] = [new]
    return redirect("/")
    
app.run(host="0.0.0.0", port=int("8080"), debug=True)