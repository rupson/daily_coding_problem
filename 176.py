#rob upson 20/5/19 daily coding problem 176

def checkForMapping(s1, s2):

    displacement = ord(s2.lower()[0]) - ord(s1.lower()[0])

    for i in range(len(s1)):
        if ord(s1.lower()[i]) + displacement == ord(s2.lower()[i]):
            continue
        else: return False

    return True

if __name__ == "__main__":

    s1 = input("enter first string: ")
    s2 = input("enter second string: ")

    print(checkForMapping(s1, s2))
