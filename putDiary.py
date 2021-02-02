import os
from evaluate import wfilter, percentWords, wordCount

def diaryOrg(entry):
    filterCheck = wfilter(entry)
    percentCheck = percentWords(entry)
    nextAvalSpot = len(os.listdir("diaries/" + str(wordCount(entry))))

    if filterCheck and percentCheck:
        diary = open(
            "diaries/" + str(wordCount(entry)) + "/" + str(nextAvalSpot) + ".txt",
            "w",
        )
        diary.write(entry)
        diary.close()
        return True
    return False
