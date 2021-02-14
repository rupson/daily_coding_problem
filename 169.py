#rob upson 13/5/19 daily programming challenge 169

class node:
    def __init__(self, data, nextNode):
        self.nextNode = nextNode
        self.data = data

    def next(self):
        return self.nextNode

    def getData(self):
        return self.data

def sort(h):
    while h.next() != None:
        if h.next().getData() < h.getData():
            tmp = h.getData()
            h.data = h.next().getData()
            h.next().data = tmp

        h = h.next() #this is not right.
        
    return h


if __name__ == "__main__":

    h = node(4, node(1, node(-3, node(99, None))))

    p = h
    
    while p.next() != None:
        print(p.getData())
        p = p.next()
    h = sort(h)
    p = h

    while p.next() != None:
        print(p.getData())
        p = p.next()
