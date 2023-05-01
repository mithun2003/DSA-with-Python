class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class Hash:
    def __init__(self, max_size):
        self.max_size = max_size
        self.table = [None] * self.max_size
        print("The table is create", len(self.table))

    def _hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        print("The index of the key is,", h % self.max_size)
        return h % self.max_size

    def insert(self, key, value):
        hash = self._hash(key)
        if self.table[hash] is None:
            self.table[hash] = Node(key, value)
            print(self.table[hash].value)
        else:
            node = self.table[hash]
            while node.next is not None:
                if node.key == key:
                    node.value = value
                    return
                node = node.next
            if node.key == key:
                node.value = value
            else:
                node.next = Node(key, value)
    def find(self,key):
        hash = self._hash(key)
        node = self.table[hash]
        while node is not None:
            if node.key == key:
                return("value at",key,node.value)
            node = node.next
        print("None")
    
    def delete(self,key):
        hash=self._hash(key)
        node = self.table[hash]
        prev =None
        while node is not None:
            if node.key ==key:
                if prev is None:
                    print(self.table[hash],self.table[hash].key)
                    self.table[hash]=node.next
                    print(node.next.key)
                else:
                    prev.next = node.next 
                return "deleted"
            prev = node
            node = node.next 
    def get_all(self):
        list = []
        for node in self.table:
            while node is not None:
                list.append((node.key, node.value))
                node = node.next
        return list


hash = Hash(10)
hash.insert("march 6", 99)
hash.insert("march 17", 199)
print(hash.find("march 6"))
print(hash.delete("march 6"))
print(hash.get_all())
