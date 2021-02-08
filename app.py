from flask import Flask, render_template, request, session, redirect, url_for
from putDiary import diaryOrg
from getDiary import getDiary
from evaluate import wordCountScore
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
os.makedirs("diaries/1", exist_ok=True)
os.makedirs("diaries/2", exist_ok=True)
os.makedirs("diaries/3", exist_ok=True)
os.makedirs("diaries/4", exist_ok=True)

@app.route("/", methods=["POST", "GET"])
def index():
    diary = None

    if request.method == "POST":
        userInput = request.form["diary"]
        if diaryOrg(userInput):
            session["diary"] = getDiary(wordCountScore(userInput))
            return redirect(url_for("diary"))

    return render_template("index.html")


@app.route("/diary", methods=["POST", "GET"])
def diary():
    diary = session.get("diary")

    return render_template("diary.html", diary=diary)

if __name__ == "__main__":
    app.run(debug=True)
