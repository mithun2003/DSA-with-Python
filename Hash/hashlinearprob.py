class HashTable:
    def __init__(self, size):
        self.size = size
        # self.keys = [None] * size
        # self.values = [None] * size
        self.table = [None]*self.size
        self.delete = object()
        self.num_items = 0
        print(object())

    def hash_function(self, key):
        return sum(ord(c) for c in key) % self.size

    def rehash(self):
        new_size = self.size * 2
        new_table = [None] * new_size
        for i in range(self.size):
            if self.table[i] is not None and self.table[i][0] is not self.delete:
                new_index = self.hash_function(self.table[i][0])
                while new_table[new_index] is not None:
                    new_index = (new_index + 1) % new_size
                new_table[new_index] = self.table[i]
        self.size = new_size
        self.table = new_table

    def insert(self, key, value):
        if self.num_items >= self.size * 0.75:
            self.rehash()

        index = self.hash_function(key)
        print(key, self.table[index] is not self.delete)
        while self.table[index] is not None and self.table[index][0] is not self.delete and self.table[index][0] != key:
            print(key, index)
            index = (index + 1) % self.size

        if self.table[index] is not None and self.table[index][0] == key:
            self.values[index] = value
        elif self.table[index] is None or self.table[index][0] is self.delete:
            self.table[index] = (key, value)
            self.num_items += 1
        # else:
        #     self.table[index] = (key,value)
        #     self.num_items += 1

    def get(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            while self.table[index] is self.delete:
                index = (index + 1) % self.size
        return None

    def remove(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (self.delete, None)
                self.num_items -= 1
                return
            index = (index + 1) % self.size

    def get_all(self):
        return [kv for kv in self.table]


h = HashTable(5)
h.insert("march 6", 99)
h.insert("march 1", 199)
h.insert("march 2", 299)
h.insert("march 3", 399)
h.insert("march 4", 499)
h.insert("march 5", 599)
print(h.get_all())
print(h.get("march 5"))
print(h.remove("march 5"))
print("GET ALL")
print(h.get("march 1"))
print(h.get("march 2"))
print(h.get("march 3"))
print(h.get("march 4"))
print(h.get("march 5"))
print(h.get("march 6"))
print(h.get_all())
h.insert("march 5", 599)
print(h.get_all())
print(h.remove("march 5"))

print(h.get_all())
# print(h.get_all())
