from wordfilter import Wordfilter
import enchant


def wfilter(entry):
    wordfilter = Wordfilter()
    if wordfilter.blacklisted(entry.lower()) == False:
        return entry
    else:
        return "oof you used a slur there buddy boy slow down"


    #check if at least half of all words are real words

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
        
