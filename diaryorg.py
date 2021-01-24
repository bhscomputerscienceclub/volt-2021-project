from evaluate import wfilter, percentwords, wordcount


def filecount(entry):
    num = open("diaries/" + str(wordcount(entry)) + "/num", "r")
    filenum = int(num.read())
    num.close()
    num = open("diaries/" + str(wordcount(entry)) + "/num", "w")
    num.write(str(filenum + 1))
    num.close()
    return filenum


def diaryOrg(entry):
    filterCheck = wfilter(entry)
    percentCheck = percentwords(entry)

    if filterCheck == True and percentCheck == True:
        diary = open(
            "diaries/" + str(wordcount(entry)) + "/" + str(filecount(entry)) + ".txt",
            "w",
        )
        diary.write(entry)
        diary.close()
