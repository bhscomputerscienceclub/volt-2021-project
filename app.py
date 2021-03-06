from flask import Flask, render_template, request, session, redirect, url_for
from putDiary import diaryOrg
from getDiary import getDiary
from evaluate import wordCountScore
import os
from distutils.dir_util import copy_tree

app = Flask(__name__)
app.secret_key = os.urandom(24)
copy_tree("example-diaries/", "diaries/")


@app.route("/", methods=["POST", "GET"])
def index():
    real = True

    if request.method == "POST":
        userInput = request.form["diary"]
        if diaryOrg(userInput):
            session["diary"] = getDiary(wordCountScore(userInput))
            return redirect(url_for("diary"))
        else:
            real=False
    return render_template("index.html", real = real)


@app.route("/diary", methods=["POST", "GET"])
def diary():
    diary = session.get("diary")

    if diary == None:
        return redirect(url_for("index"))

    return render_template("diary.html", diary=diary)

if __name__ == "__main__":
    app.run(debug=True)
