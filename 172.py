#rob upson 16/05/19 daily coding problem 172


def findSubstrings(s, words):

    cleanList = []
    for each in words:
        cleanList.append(each)
    
    checking = False
    wordLength = len(words[0])
    i = 0
    indexes = []
    while i < len(s) - wordLength:
        if s[i:i+wordLength:1] in words:
            if not checking:
                indexes.append(i)
            checking = True
            words.remove(s[i:i+wordLength:1])
            i = i + wordLength
        else:
            checking = False
            words = []
            for each in cleanList:
                words.append(each)
            i = i + 1
    return indexes

if __name__ == "__main__":

    s = "barfoobazbitbyte"
    words = ["cat", "dog"]
    
    print(findSubstrings(s, words))
