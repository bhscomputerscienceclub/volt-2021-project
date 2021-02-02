from flask import Flask, render_template, request
from evaluate import getQualityOfEntry
import os

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():

    if request.method == "POST":
        userInput = request.form.get('abc')
        inputValue  = getQualityOfEntry(userInput)

        #check if userInput is a valid input
        if inputValue != 0:
            nextAvalSpot = len(os.listdir(str(inputValue)))
            tempDir = "{}/{}.txt"
            a = open(tempDir.format(inputValue,nextAvalSpot), "w")
            a.write(userInput)
        else:
            #do somthing if userInput isn't valid
            pass

    return render_template('index.html')



    return render_template("index.html")


app.run(debug=True)