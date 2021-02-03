from flask import Flask, render_template, request
from putDiary import diaryOrg
from getDiary import getDiary
from evaluate import wordCountScore
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    diary = None

    if request.method == "POST":
        userInput = request.form['abc']
        if diaryOrg(userInput):
            diary = getDiary(wordCountScore(userInput))
            print(diary)


    return render_template('index.html')


app.run(debug=True)