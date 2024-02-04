class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

    def peek(self): 
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def display(self):
        print(self.items)


my_queue = Queue()

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

my_queue.display()

print(my_queue.dequeue())

