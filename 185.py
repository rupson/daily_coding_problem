#rob upson 4/6/2019 daily coding problem 185

def getIntersectArea(a, b):
    points_in_a = getPoints(a)
    points_in_b = getPoints(b)

    x = 0

    for point in points_in_a:
        if point in points_in_b:
            x += 1
    return x
    

def getPoints(r):
    points_in_r = []
    print(r)
    for i in range(r["top_left"][0], r["top_left"][0] + r["dimensions"][0], 1):
        for j in range(r["top_left"][1], r["top_left"][1] + r["dimensions"][1], 1):
            points_in_r.append( (i,j) )
    return points_in_r
    
    

if __name__ == "__main__":
    a = {
        "top_left": (1,4),
        "dimensions": (3,3) #width, height
        }
    b = {
        "top_left": (0,5),
        "dimensions": (4,3) #width, height
        }

    print(getIntersectArea(a,b))

        
