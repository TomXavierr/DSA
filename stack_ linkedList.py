"""Stack data structure using linked list"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            temp = self.top.data
            self.top = self.top.next_node
            return temp
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.top.data
        else:
            raise IndexError("pop from an empty stack")

    def size(self):
        current =  self.top
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count


my_stack = Stack()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print("Peeked item:", my_stack.peek())

print("Popped item:", my_stack.pop())

print("Stack size after pop:", my_stack.size())
