#rob upson 12/5/19 daily programming challenge 167


def findPalindromePairs(wordList):

    pairList = []
    
    for i in range(len(wordList)):
        for j in range(len(wordList)):
            if i == j:
                continue
            newWord = "{0}{1}".format(wordList[i], wordList[j])
            if newWord[::-1] == newWord:

                print("reverse: " + newWord[::-1])
                print("comparator: " + newWord)
                pairList.append((i,j))

    return pairList



if __name__ == "__main__":

    wordList = ["code", "edoc", "da", "d"]
    
    print(findPalindromePairs(wordList))
