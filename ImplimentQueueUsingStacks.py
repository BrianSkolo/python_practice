# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]

# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false

# queue: first in first out (FIFO).  in order adding: q = [a,b,c] removing q = [-a, -b, -c]
class MyQueue:
    
    def __init__(self):   
# initialize your data structure here by creating two stacks (empty lists), stack one and stack two:
        self.stackOne = [] 
        self.stackTwo = []

# stackOne will be our main stack, the second stack is where we store values that will be pushed back to our first stack
# push element/ item x to the back of the queue:     
    def push(self, x: int) -> None:
# while there are values in stackOne, we want to pop those values and store them in stackTwo
        while self.stackOne:
             self.stackTwo.append(self.stackOne.pop())
# now we can append a new value to stackOne
        self.stackOne.append(x)
# while there are values in stackTwo, pop the values and put them back in stackOne
        while self.stackTwo:
            self.stackOne.append(self.stackTwo.pop())
             
# removes element/ item from the queue and returns that element        
    def pop(self) -> int:
        return self.stackOne.pop()

# get the front element/ item from the queue                
    def peek(self) -> int: 
        return self.stackOne[-1]

# returns whether the queue is empty or not    
    def empty(self) -> bool:
        not self.stackOne