class MyCircularQueue:

    def __init__(self, k: int):
#         head, tail (head points at beginning of queue, tail points at the end of the queue:  tail inreases when we append and head descreases/ deque/ pops off the end ).  Tail keeps track of where we can add values

#          size of our queue  , how many we've added how many we've poppped off.  Once the size is equal the the max allowed in array (k) the we know its full.  if the size is 0 its empty and we can't pop anything else off.
        self.head = 0
        self.tail = 0 
        self.size = 0
        self.k = k 
        self.q = [None] * k
#         k is the max size of our queue.  q is our list [None] * k represents how many values we can have.

#         when dequeueing we need to check if the queue is full or not, if it's full we can't add anything.
    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.size += 1
        self.q[self.tail+1] = value 
#         How to handle what we do when the tail wraps around.  if it hits the end of the queue max size (k).  This makes sure that once we hit the end of the queue if we add another item (tail) that we put it on position 0 in the queue.  self.size += 1: increase size queue?
        self.tail = (self.tail+1)%self.k
        return True
        

#         same as enQueue but decrease q size (self.size -= 1) and utilize head instead of tail (head: take an item off at the beginning of the queue, tail add somethign at the end)
    def deQueue(self) -> bool:
        if self.isEmpty(): return False        
        self.size -= 1
        # self.q[self.head] = value   unneccessary because we aren't returning any values here (we are removing a value )
        self.head = (self.head+1)%self.k
        

    def Front(self) -> int:
#         of the item is empty we can't return andthing so we use return -1
        if self.isEmpty(): return -1
        return self.q[self.head]
#         returns the front item in the queue or returns nothing (return - 1), takes the front item from the q and returns it's index

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.q[self.tail-1]
    #         returns the last item in the queue or returns nothing (return - 1), takes the last item from the q and returns it's index.  tail-1 looks at the value right before it

    def isEmpty(self) -> bool:
        if self.size == 0: return True
        return False
#     if the queue is empty returned true, if it's not return falsF

    def isFull(self) -> bool:
        if self.size == self.k: return True
        return False
#         if the size of the queue is maxed out(if the queue is full) then return true.  If it's not full then return false

# not quite sure how the modulator operator works (%)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()