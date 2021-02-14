#rob upson 21/5/19 daily coding problem 177


class node:
    def __init__(self, _data, _next):
        self.data = _data
        self.next = _next

    def setNext(self,n):
        self.next = n

    def setData(self,d):
        self.data = d

def rotate(p, k):


    while p.next != None:

        for i in range(k):
            swapNext(p)
        p = p.next
    
    return p
    

def swapNext(p):
    if p.next != None:
        data = p.data
        p.setData(p.next.data)
        p.next.setData(data)
    

if __name__ == "__main__":

    k = 2
    h = node(7,
             node(7,
                  node(3,
                       node(5, None)
                       )
                  )
             )
    
    
    p = rotate(h, k)

    while p.next != None:
        print("{0} -> ".format(p.data))
        p = p.next
