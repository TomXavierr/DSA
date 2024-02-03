"""Stack using list"""

class stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return IndexError("peek from an  empty stack")

    def size (self):
        return len(self.items)


my_stack = stack()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print("Stack:", my_stack.items)

print(my_stack.pop())

print(my_stack.peek())

