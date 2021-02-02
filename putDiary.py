from evaluate import wfilter, getQualityOfEntry, wordcount as wordCount
import os

# This is useless now. uncomment if needed

# def fileCount(entry):
#     num = open("diaries/" + str(wordCount(entry)) + "/num", "r")
#     filenum = int(num.read()) + 1
#     num.close()
#     num = open("diaries/" + str(wordCount(entry)) + "/num", "w")
#     num.write(str(filenum))
#     num.close()
#     return filenum


# use this method in the flask thing prob
def putDiary(entry):
    fileCount = len(os.listdir("diaries/" + str(wordCount(entry))))
    diary = open(
        "diaries/" + str(wordCount(entry)) + "/" + str(fileCount + 1),
        "w",
    )
    diary.write(entry)
    diary.close()
