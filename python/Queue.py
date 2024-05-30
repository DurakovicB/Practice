class Queue:
    def __init__(self):
        self.array=[]
    def length(self):
        return len(self.array)
    def push(self,value):
        self.array.append(value)
    def pop(self):
        result=self.array[0]
        self.array=self.array[1:]
        return result
queue=Queue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
queue.push(5)
for i in range(5):
    print(queue.array)
    print(queue.pop())

    
