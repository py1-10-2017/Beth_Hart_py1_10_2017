from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def greeting():
    return render_template("index.html")
    
@app.route("/ninjas")
def ninjas():
    return render_template("ninjas.html")
    
@app.route("/dojo/new")
def dojos():
    return render_template("dojos.html")

app.run(host="0.0.0.0", port=int("8080"),debug=True)