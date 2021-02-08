import random, os

# gets a random diary of quality quality
# use this in the flask thing
def getDiary(quality):
    rand = random.randint(0, len(os.listdir("diaries/" + str(quality))) - 2)
    diary = open("diaries/" + str(quality) + "/" + str(rand))
    content = diary.read()
    diary.close()
    return content
