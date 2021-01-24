from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():

    if request.method == "POST":
        a = open("input.txt", "w")
        a.write(request.form.get("abc"))

    return render_template("index.html")


app.run(debug=True)