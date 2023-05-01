class TrieNode:
    def __init__(self):
        self.dict = {}
        self.endString = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self,word):
        current = self.root
        for i in word:
            ch = i
            node = current.dict.get(ch)
            if node is None:
                node = TrieNode()
                current.dict.update({ch:node})
            current = node
        current.endString = True
        
    def Search(self,word):
        current = self.root
        for i in word:
            node = current.dict.get(i)
            if node is None:
                return False
            current = node
        if current.endString == True:
            return True
        else:
            return False
        
    def remove(self,word):
        def _remove(node,word,index):
            if index == len(word):
                node.endString = False
                return len(node.dict)==0
            ch = word[index]
            if ch not in node.dict:
                return False
            shouldDelete = _remove(node.dict[ch],word,index+1)
            if shouldDelete:
                del node.dict[ch]
                return len(node.dict)==0
            return False
        _remove(self.root,word,0)
        
        
trie = Trie()
trie.insert("iiile")
trie.insert("app")
trie.insert("apis")
trie.insert("api")
print(trie.Search("api"))
trie.remove("api")
print(trie.Search("api"))
print(trie.root.dict)