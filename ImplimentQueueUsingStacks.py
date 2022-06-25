class MyQueue:

    def __init__(self):
        self.stackOne = []
        self.stackTwo = []

    def push(self, x: int) -> None:
        self.stackOne.append(x)
        while self.stackOne:
            self.stackTwo.append(self.stackOne.pop())
        while self.stackTwo:
            self.stackOne.append(self.stackTwo.pop())
        
    def pop(self) -> int:
        return self.stackOne.pop(0)

    def peek(self) -> int:
        return self.stackOne[0]
        

    def empty(self) -> bool:
        return not self.stackOne 

        # [null,null,null,1,1,false]
        # [null,null,null,1,2,false]