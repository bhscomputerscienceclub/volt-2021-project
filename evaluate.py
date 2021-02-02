from wordfilter import Wordfilter
import enchant
import wordfilter

# returns true if the message doesn't contain a blacklisted word
def wfilter(entry):
    wordfilter = Wordfilter()
    if wordfilter.blacklisted(entry.lower()) == False:
        return True
    else:
        return False



#check if at least 3/4 of all words are real words
def percentwords(entry):
    dictionary = enchant.Dict("en_US")
    wlist = entry.split()
    realWordCount = 0
    for i in wlist:
        if dictionary.check(i) ==True:
            realWordCount += 1
    
    if realWordCount / len(wlist) >= 0.75 :
        return True
            
    return False
        
#define a scre for the length of the input
def wordcount(entry):
    wlist =  entry.split()

    if len(wlist) < 15:
        return 1
    elif len(wlist) < 30:
        return 2
    elif len(wlist) < 75:
        return 3
    else:
        return 4

#puts all of the previus methods together, if it returns 0 then that means the entry did not pass
def getQualityOfEntry(entry):
    if wfilter(entry) and percentwords(entry):
        return wordcount(entry)
    return 0
