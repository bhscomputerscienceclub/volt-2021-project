from evaluate import wfilter, percentWords, wordCount


def fileCount(entry):
    num = open("diaries/" + str(wordCount(entry)) + "/num", "r")
    filenum = int(num.read())
    num.close()
    num = open("diaries/" + str(wordCount(entry)) + "/num", "w")
    num.write(str(filenum + 1))
    num.close()
    return filenum


def diaryOrg(entry):
    filterCheck = wfilter(entry)
    percentCheck = percentWords(entry)

    if filterCheck == True and percentCheck == True:
        diary = open(
            "diaries/" + str(wordCount(entry)) + "/" + str(fileCount(entry)) + ".txt",
            "w",
        )
        diary.write(entry)
        diary.close()
