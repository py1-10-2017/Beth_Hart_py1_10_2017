from flask import Flask, render_template, redirect, request, flash, session
app = Flask(__name__)
app.secret_key='perma frosting'

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/result', methods=["POST"])
def show_user():
    result = request.form #save the form input object in var called result
    if len(request.form["name"]) < 1:
        flash("Please enter a valid name")
    else:
        flash("Thank you, {}".format(request.form["name"]))
    if len(request.form["comments"]) < 1 or len(request.form["comments"]) > 120:
        flash("Comments are required and have a max of 120 characters.")
    else:
        flash("Thank you for the comments!")
    return redirect("/") 
    
       


app.run(host="0.0.0.0", port=int('8080'), debug=True)
# app.run(debug=True)