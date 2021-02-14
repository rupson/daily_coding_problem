#rob upson 16/05/19 daily coding problem 171

import random

def findBusiestTime(logs):

    currentInBuilding = 0
    highest = 0
    start = 0
    end = 0
    
    for each in logs:
        print("{0} - {1} :: {2}".format(logs.index(each), each, currentInBuilding))
        if each["type"] == "enter":
            currentInBuilding += each["count"]
            if currentInBuilding >= highest:
                highest = currentInBuilding
                start = each["timestamp"]
                
        else:
            if currentInBuilding >= highest:
                highest = currentInBuilding
                end = each["timestamp"]
            currentInBuilding -= each["count"]

##        print("current people: {0}".format(currentInBuilding))

    return (start, end, highest)

def generateLogs():
    logs = []
    logNumber = 5000
    currentIn = 0
    lastTimestamp = 1526579928

    for i in range(logNumber):
        
        timestamp = random.randint(lastTimestamp, lastTimestamp + 1200)
        lastTimestamp = timestamp
        
        count = random.randint(1,10)

        choice = random.choice(["enter","exit"])

        if currentIn < 1:
            choice = "enter"
        elif choice == "exit" and count > currentIn:
            count = currentIn

        if i == logNumber -1:
            if currentIn != 0:
                choice = "exit"
                count = currentIn
            else:
                break

        if choice == "enter":
            currentIn += count
        else:
            currentIn -= count

        logs.append( {"timestamp": timestamp,
                          "count":count,
                          "type": choice } )

    return logs

if __name__ == "__main__":

    logs = generateLogs()

    print(findBusiestTime(logs))
