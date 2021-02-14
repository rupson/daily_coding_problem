import random

def weightedProb(numbers, weights):
    array100 = []
    for i in range(len(weights)):
        for j in range(int(100*weights[i])):
            array100.append(numbers[i])
    return array100[random.randint(0,99)]

if __name__ == "__main__":
    numbers = [1,2,3,4]
    weights=[0.1,0.5,0.2,0.2]
    print(weightedProb(numbers,weights))
