class Hash:
    def __init__(self, size):
        self.size = size
        self.table = [None]*self.size
        self.count = 0
        self.delete = object()

    def _hash(self, key):
        return sum(ord(c) for c in key) % self.size

    def insert(self, key, value):
        if self.count >= 0.7 * self.size:
            self.rehash()
        h = self._hash(key)
        while self.table[h] is not None and self.table[h][0] != key and self.table[h] is not self.delete:
            h = (h+1) % self.size
        if self.table[h] is None:
            self.count += 1
            self.table[h] = (key, value)

    def rehash(self):
        new_size = self.size * 2
        new_table = [None]*new_size
        for i in range(self.size):
            if self.table[i] is None:
                continue
            key, value = self.table[i]
            j = self._hash(key)
            while new_table[j] is not None and new_table[j][0] != key:
                j = (j+1) % new_size
            new_table[j] = (key, value)
        self.size, self.table = new_size, new_table

    def remove(self, key):
        h = self._hash(key)
        while self.table[h] is not None:
            if self.table[h][0] == key:
                self.table[h] = self.delete
                self.count -= 1
                return
            h = (h + 1) % self.size

    def get(self, key):
        h = self._hash(key)
        while self.table[h] is not None:
            if self.table[h][0] == key:
                if self.table[h] is not self.delete:
                    return self.table[h][1]
                else:
                    h = (h+1) % self.size
            else:
                h = (h+1) % self.size
        return None

    def get_all(self):
        return [kv for kv in self.table]
h = Hash(5)
h.insert("march 6", 99)
h.insert("march 1", 199)
h.insert("march 2", 299)
h.insert("march 3", 399)
h.insert("march 4", 499)
h.insert("march 5", 599)
print(h.get_all())
print(h.get("march 5"))
print(h.remove("march 5"))
print(h.get("march 2"))
print(h.get_all())
# print(h.get_all())
