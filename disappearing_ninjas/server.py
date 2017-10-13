from flask import Flask, request, redirect, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route('/ninja')
def group():
    images = ["/static/images/leonardo.jpg",
    "/static/images/raphael.jpg", "/static/images/michelangelo.jpg",
        "/static/images/donatello.jpg"]
    return render_template("ninjas.html", images=images)
    
@app.route("/ninja/<color>")
def solo(color):
    if color == "blue":
        images=["/static/images/leonardo.jpg"]
    elif color == "red":
        images=["/static/images/raphael.jpg"]
    elif color == "orange":
        images=["/static/images/michelangelo.jpg"]
    elif color == "purple":
        images=["/static/images/donatello.jpg"]
    else:
        images=["/static/images/notapril.jpg"]
    return render_template("ninjas.html", images=images)

app.run(host="0.0.0.0", port=int("8080"), debug=True)