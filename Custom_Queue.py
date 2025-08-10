class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self,item):
        self.q.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.q.pop(0)   
    
    def is_empty(self):
        return len(self.q) == 0

    def front(self):
        return self.q[0]
    
    def display(self):
     return self.q
