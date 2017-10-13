from flask import Flask, request, redirect, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route('/ninja')
def group():
    images = ["leonardo", "raphael", "michelangelo", "donatello"]
    return render_template("ninjas.html", images=images)
    
@app.route("/ninja/<color>")
def solo(color):
    if color == "blue":
        images=["leonardo"] 
    elif color == "red":
        images=["raphael"] 
    elif color == "orange":
        images=["michelangelo"] 
    elif color == "purple":
        images=["donatello"] 
    else:
        images=["notapril"] 
    return render_template("ninjas.html", images=images)

app.run(host="0.0.0.0", port=int("8080"), debug=True)