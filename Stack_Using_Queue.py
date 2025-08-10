# Stack (LIFO) using Queue

from Custom_Queue import Queue

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, item):
        while not self.q1.is_empty():
            self.q2.enqueue(self.q1.dequeue())  # move all data q1 → q2

        self.q1.enqueue(item)  # add new item to q1

        while not self.q2.is_empty():
            self.q1.enqueue(self.q2.dequeue())  # move all data back q2 → q1

    def display(self):
        for i in self.q1.display():
            print(i)

    def top(self):
        if not self.q1.is_empty():
            return self.q1.front()
        else:
            print("Stack is Empty !!!")
            return None

    def pop(self):
        if not self.q1.is_empty():
            return self.q1.dequeue()
        else:
            print("Stack is Empty !!!")
            return None

    def is_empty(self):
        return self.q1.is_empty()

s = Stack()
print("Check stack empty", s.is_empty())

s.push(1)
s.push(2)
s.push(3)
print("\nAfter items pushed:")
s.display()
print("Top element is:", s.top())
print("Is stack empty", s.is_empty())

print("\nPopped Element is:", s.pop())
print("After pop:")
s.display()
print("Top element is:", s.top())
print("Is stack empty?", s.is_empty())
