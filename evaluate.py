from wordfilter import Wordfilter
import enchant

# returns true if the message doesn't contain a blacklisted word
def wfilter(entry):
    wordfilter = Wordfilter()
    if wordfilter.blacklisted(entry.lower()) == False:
        return True
    else:
        return False


# check if at least 3/4 of all words are real words
def percentWords(entry):
    dictionary = enchant.Dict("en_US")
    wlist = entry.split()
    realWordCount = 0
    for i in wlist:
        if dictionary.check(i) == True:
            realWordCount += 1

    if realWordCount / len(wlist) >= 0.75:
        return True

    return False


# define a scre for the length of the input
def wordCountScore(entry):
    wlist = entry.split()

    if len(wlist) < 15:
        return 1
    elif len(wlist) < 30:
        return 2
    elif len(wlist) < 75:
        return 3
    else:
        return 4
