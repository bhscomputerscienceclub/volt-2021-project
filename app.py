from flask import Flask, render_template, request
from putDiary import diaryOrg

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():

    if request.method == "POST":
        userInput = request.form.get('abc')
        
        if diaryOrg(userInput):
            print("sucess")
        else:
            print("fail")

    return render_template('index.html')


app.run(debug=True)