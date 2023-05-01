class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
class Hash:
    def __init__(self,size):
        self.size = size
        self.table = [None]*self.size
        
    def _hash(self,key):
        return sum(ord(c) for c in key)%self.size
    
    def insert(self,key,value):
        h = self._hash(key)
        if self.table[h] is None:
            self.table[h] = Node(key,value)
        else:
            node = self.table[h]
            while node.next is not None:
                if node.key == key:
                    node.value = value
                    return
                node = node.next 
            if node.key ==key:
                node.value = value
            else:
                node.next = Node(key,value)
                
    
    def get(self,key):
        h = self._hash(key)
        while self.table[h] is not None:
            if self.table[h].key==key:
                return self.table[h].value
            self.table[h]=self.table[h].next
        return None
    
hash = Hash(10)
hash.insert("march 6", 99)
hash.insert("march 17", 199)
hash.insert("march 7", 299)
hash.insert("march 107", 1099)
hash.insert("march 187", 1899)
hash.insert("march 197", 1999)
hash.insert("march 177", 1799)
hash.insert("march 1777", 17799)
hash.insert("march 1977", 174499)
hash.insert("march 134777", 1744799)

print(hash.get("march 6"))
print(hash.get("march 17"))
print(hash.get("march 7"))
print(hash.get("march 107"))
print(hash.get("march 187"))
print(hash.get("march 197"))
print(hash.get("march 177"))
print(hash.get("march 1777"))
print(hash.get("march 1977"))
print(hash.get("march 134777"))
# print(hash.delete("march 6"))
# print(hash.get_all())
        