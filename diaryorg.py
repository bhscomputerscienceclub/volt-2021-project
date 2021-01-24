from evaluate import wfilter, percentwords, wordcount

# do soon def filecount 

def diaryOrg(entry):
    filterCheck = wfilter(entry)
    percentCheck = percentwords(entry)


    if filterCheck == True and percentCheck == True:
        diary = open("diaries/" + str(wordcount(entry))+ "/" + "1.txt", "w")
        diary.write(entry)
