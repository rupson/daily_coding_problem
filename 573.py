def interweave(stack):
    max_pointer = len(stack)
    pointer = 1
    queue = []
    while pointer < max_pointer:
        while len(stack) > pointer:
            queue.append(stack.pop()) ##pop items in stack and enqueue them
        while len(queue) > 0:
            stack.append(queue.pop(0)) ##dequeue items into stack
        pointer+=1
    return stack

if __name__ == "__main__":
    stack = [1,2,3,4,5,6,7]
    print(interweave(stack))