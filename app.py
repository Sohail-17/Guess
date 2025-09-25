from flask import Flask, render_template
from flask import request
from minigames import wordguess
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/npat")
def npat():
    return render_template("npat.html")

@app.route("/wordguess", methods=["GET", "POST"])
def wordguess_route():
    result = None
    if request.method =="POST":
        guess = request.form.get("guess")
        result = wordguess.check_guess(guess)
    return render_template("wordguess.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
