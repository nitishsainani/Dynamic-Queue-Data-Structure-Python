class Queue:
    def __init__(self):
        self.size = 10
        self.arr = [0 for _ in range(10)]
        self.front = -1
        self.rear = 0
        self.n = 0
    
    def __reverse__(self, i, j):
        while i < j:
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            i += 1
            j -= 1

    def __rotate__(self, start = 0, point = None, end = None):
        if point is None:
            point = self.front
        if end is None:
            end = self.size - 1
        self.__reverse__(start, point)
        self.__reverse__(point+1, end)
        self.__reverse__(start, end)

    def __expand__(self):
        newSize = self.size * 10
        self.arr.extend([0 for _ in range(newSize - self.size)])
        self.__rotate__()
        self.rear = 0
        self.front = self.size - 1
        self.size = newSize

    def isEmpty(self):
        return self.n == 0

    def peek(self):
        # check underflow
        if (self.front + 1)%self.size == self.rear and self.n == 0:
            return -1
        return self.arr[self.rear]

    def peek_rear(self):
        # check underflow
        if (self.front + 1)%self.size == self.rear and self.n == 0:
            return -1
        return self.arr[self.front]

    def pop(self):
        # Checking underflow condition
        if (self.front + 1)%self.size == self.rear and self.n == 0:
            return False
        val = self.arr[self.rear]
        self.rear = (self.rear+1)%self.size
        self.n -= 1
        return val

    def push(self, x):
        # check overflow condition
        if (self.front + 1)%self.size == self.rear and self.n != 0:
            self.__expand__()
        self.front = (self.front+1) % self.size
        self.arr[self.front] = x
        self.n += 1
