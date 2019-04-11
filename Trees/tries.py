__author__ = 'rdhek'

class Trie:
    def __init__(self):
        eofFlag=0
        count=0
        listOfAlphbets=[]
    def insertNode(self,word):
        temp = self
        for el in word:
            if el != self.listOfAlphbets[el-'a']:
                newTrie=Trie(self)
                newTrie.count=newTrie.count+1
                self.listOfAlphbets

