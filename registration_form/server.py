from flask import Flask, session, render_template, redirect, request, flash

app=Flask(__name__)
app.secret_key="little plastic thingy"

@app.route('/', methods=["get", "POST"])
def form():
    return render_template("index.html")
    
@app.route("/register", methods=["POST"])
def reg():
    result = request.form
    error = False
    if len(result["first_name"]) < 1 or len(result["last_name"]) < 1:
        flash("ERROR: first and last name are required")
        error = True
    if not result["first_name"].isalpha() or not result["last_name"].isalpha():
        flash("ERROR: first and last name must be letters only")
        error = True
    if len(result["password"]) < 8:
        flash("ERROR: password must be at least 8 charachters")
        error = True
    if result["password"] != result["conf_password"]:
        flash("ERROR: passwords do not match")
        error = True
    if error == False:
        return "THANK YOU FOR COMPLETEING THE REGISTRATION"
    return redirect('/')


app.run(host="0.0.0.0", port=int("8080"), debug=True)