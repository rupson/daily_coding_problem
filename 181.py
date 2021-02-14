#rob upson 25/5/19 daily coding problem 181

def findPalindromes(inputString):
    s = "{0}".format(inputString)
    stringList = []
    loopCount = 0
    
    while len(s) > 0:
        loopCount+=1
        n = 0
        while (s[len(s)-1-n::-1] != s[0:len(s)-n:1]) and (n <= len(s)):
            #print("{0} :: {1}".format(s[0:len(s)-n:1],s[len(s)-n::-1]))
            n = n+1
            loopCount += 1
        stringList.append(s[0:len(s)-n:1])
        s = s[len(s)-n:len(s):1]

    print(loopCount)
    return stringList

if __name__ == "__main__":
    inputString = ""
    while inputString != "q":
        inputString = input("enter your string: ")
        print(findPalindromes(inputString))
