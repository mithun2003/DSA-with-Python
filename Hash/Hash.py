class HashTable:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.data_list = [None]*self.maxsize

    def _hash(self, key):
        h = 0
        for i in key:
            h += ord(i)

        # print(h % len(self.data_list))
        return h % len(self.data_list)

    def insert(self, key, value):
        h = self._hash(key)
        print(h)
        if self.data_list[h] is None:
            self.data_list[h] = []
        self.data_list[h].append((key, value))

    def get(self, key):
        h = self._hash(key)
        res = self.data_list[h]
        for k, value in res:
            if k == key:
                # key , value = res
                return key, value
        return None

    def delete(self, key):
        h = self._hash(key)
        res = self.data_list[h]
        if res is not None:
            for i, (k, value) in enumerate(res):
                if k == key:
                    del res[i]
                    return ("deleted")
        return ("Key not Found")

    def get_all(self):
        list = [kv for kv in self.data_list]
        return list


hash = HashTable(10)
hash.insert("march 17", 88)
hash.insert("march 37", 88)
hash.insert("march 5", 88)
hash.insert("march 6", 8)
print(hash.get_all())
print(hash.get("march 17"))
print(hash.delete("march 6"))
print(hash.get_all())
