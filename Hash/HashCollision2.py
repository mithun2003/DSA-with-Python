class Hash:
    def __init__(self, size):
        self.size = size
        self.table = [None]*self.size
        self.count = 0

    def _hash(self, key):

        return sum(ord(c) for c in key) % self.size

    def insert(self, key, value):
        if self.count >= self.size*0.7:
            self.rehash()
        h = self._hash(key)
        print("hash", h)
        # if self.table[h] is None:
        #     self.table[h] = (key, value)
        #     self.count += 1
        # else:
        i = 0
        while h < self.size:
            slot = (h + i) % self.size
            if self.table[slot] is None:
                self.table[slot] = (key, value)
                self.count += 1
                return
            elif self.table[slot][0] == key:
                self.table[slot] = (key, value)
                return
            else:
                i += 1
        print("Created")

    def rehash(self):
        new_size = self.size * 2
        new_table = [None]*new_size
        for i in range(self.size):
            if self.table[i] is None:

                continue
            key, value = self.table[i]
            j = self._hash(key)
            print("REHASH", j)
            while new_table[j] is not None and new_table[j][0] != key:
                j = (j+1) % new_size

            new_table[j] = (key, value)

        self.size = new_size
        self.table = new_table

    def find(self, key):
        h = self._hash(key)
        i = h
        # print(i, h)
        while self.table[i] is not None:
            # print("I and H are", i)
            # if self.table[i] is None:
            #     return None
            if self.table[i][0] == key:
                return self.table[i][1]
            else:
                i = (i+1) % self.size
        return None
    

    def find_by_value(self, value):
        find_by_value = []
        for kv in self.table:
            if kv is not None and kv[1] == value:
                find_by_value.append((kv[0], kv[1]))
        if find_by_value:
            return ("The key and value are", find_by_value)
        else:
            return ("Not found")

    def get_all(self):
        list = [kv for kv in self.table]
        print(list)

    def get_values(self):
        return [pair[1] for pair in self.table if pair is not None]
    def get_keys(self):
        return [pair[0] for pair in self.table if pair is not None]
has = Hash(1)
has.insert("march 6", 99)
has.insert("march", 99)
has.insert("mt", 599)
has.insert("mti", 899)
has.insert("mi", 999)
has.insert("m0", 199)
has.insert("muy", 299)
has.insert("mgh", 399)
print(has.find("mgh"))
# print(has.find_by_value(99))
print(has.get_values())
print(has.get_keys())
has.get_all()
