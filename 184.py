#rob upson 4/6/19 daily coding problem 184

def greatestCommonDenom(a):
    a.sort()
    x = a[0]
    found = False
    while x > 1 and not found:
        for each in a:
            if (each / x) % 1 != 0:
                x -= 1
                found = False
                break
            found = True
    return x
        

if __name__ == "__main__":
    a = [42,56,14, 7, 21, 70, 77]
    print(greatestCommonDenom(a))
