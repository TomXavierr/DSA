class HashTable:
    def __init__(self, size=7):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def custom_hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.table)
        return my_hash

    def print_table(self):
        for i,val in enumerate(self.table):
            print(i," : ",val)

    def set_item(self, key, value):
        index = self.custom_hash(key)
        if self.table[index] == None:
            self.table[index] = []
        self.table[index].append([key,value])

    def get_item(self, key):
        index = self.custom_hash(key)
        if self.table[index]:
            for i, element in enumerate(self.table[index]):
                if element[0] == key:
                    return self.table[index][i][1]

    def delete_item(self, key):
        index = self.custom_hash(key)

        if not self.table[index]:
            raise KeyError(f'{key} not found in the table')

        for i, elements in enumerate(self.table[index]):
            if elements[0] == key:
                
                del self.table[index][i]
        

        




hash_table = HashTable()

hash_table.set_item("name", "john")
hash_table.set_item("age", 25)
hash_table.set_item("likes", 2454)
# hash_table.set_item("age", 25)
# hash_table.set_item("age", 25)
# hash_table.set_item("age", 25)
# hash_table.set_item("age", 25)




hash_table.print_table()
print(hash_table.get_item("age"))

hash_table.delete_item("age")

hash_table.print_table()