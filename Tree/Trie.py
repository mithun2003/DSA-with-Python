class Node:
    def __init__(self):
        self.dict = {}
        self.endString = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insertString(self, string):
        current = self.root
        for i in string:
            ch = i
            node = current.dict.get(ch)
            if node is None:
                node = Node()
                current.dict.update({ch: node})
            current = node
        current.endString = True

    def searchString(self, word):
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

    def deleteString(self, word):
        def _delete(node,word,index):
            if index == len(word):
                node.endString = False
                return len(node.dict)==0
            ch = word[index]
            if ch not in node.dict:
                return False
            shouldDeleteCurrent = _delete(node.dict[ch],word,index+1)
            if shouldDeleteCurrent:
                del node.dict[ch]
                return len(node.dict)==0
            return False
        _delete(self.root,word,0)

trie = Trie()
trie.insertString("iiile")
# trie.insertString("app")
trie.insertString("apis")
trie.insertString("api")
print(trie.searchString("api"))
trie.deleteString("iiile")
print(trie.searchString("api"))
print(trie.root.dict)

