import os
from evaluate import wfilter, percentWords, wordCountScore

def diaryOrg(entry):
    filterCheck = wfilter(entry)
    percentCheck = percentWords(entry)
    nextAvalSpot = len(os.listdir("diaries/" + str(wordCountScore(entry))))

    if filterCheck and percentCheck:
        diary = open(
            "diaries/" + str(wordCountScore(entry)) + "/" + str(nextAvalSpot),
            "w",
        )
        diary.write(entry)
        diary.close()
        return True
    return False
