class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev_node = None
        self.next_node = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is none

    def append(self, data):
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node


    def prepend(self, data):
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
            self.head =  new_node

    def delete(self, data):
        current = self.head

        while current and current.data != data:
            current = current.next_node

        if current:
            if current.prev_node:
                current.prev_node.next_node = current.next_node
            else:
                self.head = current.next_node

            if current.next_node:
                current.next_node.prev_node = current.prev_node
            else:
                self.tail =  current.prev_node
        
    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next_node
        print("None")

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev_node
        print("None")



linked_list = DoublyLinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

linked_list.display_forward()
linked_list.display_backward()


linked_list.prepend(4)
linked_list.prepend(5)
linked_list.prepend(6)


linked_list.display_forward()
linked_list.display_backward()

linked_list.delete(5)

linked_list.display_forward()
# linked_list.display_backward()