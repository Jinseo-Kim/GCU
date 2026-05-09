MAX_QSIZE = 10

class Queue:
    def __init__(self) :
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE
        self.flag = 0

    def isEmpty(self) : 
        # return self.front == self.rear
        return (self.front == self.rear and self.flag == 0)

    def isFull1(self) : 
        return self.front == (self.rear + 1) % MAX_QSIZE
    
    def isFull2(self):
        return (self.front == self.rear and self.flag == 1)

    def clear(self) : 
        self.front = self.rear

    def enqueue(self, item):
        if not self.isFull2() :
            self.rear = (self.rear + 1) % MAX_QSIZE
            self.items[self.rear] = item
            self.flag = 1

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % MAX_QSIZE
            self.flag = 0
        else:
            print("Queue is Empty")

        return self.items[self.front] ## isEmpty == True: None

    def peek(self):
        if not self.isEmpty() :
            return self.items[(self.front + 1) % MAX_QSIZE]
        
    def display(self):
        out = []
        if self.front < self.rear :
            out = self.items[self.front+1:self.rear+1]
        else :
            out = self.items[self.front+1:MAX_QSIZE] + self.items[0:self.rear+1]
        # print("[f=%s, r=%d] ->" %(self.front, self.rear), out)
        print(f'[f={self.front}, r={self.rear}] -> {out}')

q = Queue()
for i in range(5):
    q.enqueue(i)

q.display()