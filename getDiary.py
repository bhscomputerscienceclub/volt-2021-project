import random, os
from evaluate import wordcount

# gets a random diary of quality quality
# use this in the flask thing
def getDiary(quality):
    rand = random.randint(1, len(os.listdir("diaries/" + str(quality))))
    diary = open("diaries/" + str(quality) + "/" + str(rand))
    content = diary.read()
    diary.close()
    return content
