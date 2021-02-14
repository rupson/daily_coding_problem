#rob upson 12/5/19 daily programming challenge 168


def rotate(matrix):
    matrixList = []
    newMatrix = []
    
    for i in range(len(matrix)):
        row = []
        for each in matrix:
            row.append(each[i])
        row.reverse()
        newMatrix.append(row)

    for each in matrix: 
        print(each)

    return newMatrix


if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    rotated = rotate(matrix)
    print()
    for each in rotated:
        print(each)
