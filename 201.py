#rob upson 14/6/2019 daily coding problem 201

def findMaxPath(t):
    i = len(t) -1
    total = 0
    j = getMax(t[len(t)-1])
    while i > 0:
        total += t[i][j];
        if j > 0:
            if j != len(t[i-1]):
                if t[i-1][j-1] > t[i-1][j]:
                    j -= 1
            else: j -= 1
        i -= 1
    total += t[i][j];
    return total

def getMax(a):
    highest = -1
    maxIndex = -1
    for i in range(len(a)):
        if a[i] > highest:
            highest = a[i]
            maxIndex = i
    return maxIndex
        

if __name__ == "__main__":
    triangle = [[1],[2,3],[1,5,1],[100,1,1,1]]
    print(findMaxPath(triangle))
