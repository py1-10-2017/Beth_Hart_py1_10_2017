from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/result', methods=["POST"])
def show_user():
    result = request.form #save the form input object in var called result
    return render_template("new.html", result = result) #render the template and pass in the result object
    
       


app.run(host="0.0.0.0", port=int('8080'), debug=True)
# app.run(debug=True)