'''
["Trie","insert","search","search","startsWith","insert","search"]
[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]

["Trie","insert","startsWith"]
[[],["hotdog"],["dog"]]
'''

class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def insert(self, word: str) -> None:
        
        cur = self
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
                
            cur = cur.children[c]
        cur.isWord = True
    
    def search(self, word: str) -> bool:
        
        cur = self
        
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return cur.isWord
    
    def startsWith(self, prefix: str) -> bool:
        
        cur = self
        
        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return True



'''First Approach-------------------------------------'''
# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.isWord = False
        

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
        
#     def insert(self, word: str) -> None:
        
#         cur = self.root
        
#         for c in word:
#             if c not in cur.children:
#                 cur.children[c] = TrieNode()
            
#             cur = cur.children[c]
        
#         cur.isWord = True            
                
#     def search(self, word: str) -> bool:
        
#         cur = self.root
        
#         for c in word:
#             if c in cur.children:
#                 cur = cur.children[c]
#             else:
#                 return False
        
#         return cur.isWord
            
#     def startsWith(self, prefix: str) -> bool:
        
#         cur = self.root
        
#         for c in prefix:
#             if c in cur.children:
#                 cur = cur.children[c]
#             else:
#                 return False
        
#         return True
        
            
        
'''My first attempt-------------------------------------------------------------'''
#     def __init__(self):
#         self.d = {}
#         self.is_word = False

#     def insert(self, word: str) -> None:
        
#         if len(word) == 1:
            
#             c = word[0]
            
#             if c in self.d:
#                 if self.d[c].is_word == False:
#                     self.d[c].is_word = True
#             else:
#                 self.d[c] = Trie()
#                 self.d[c].is_word = True
                    
#         for i in range(len(word)-1):
            
#             c = word[i]
            
#             if c in self.d:
#                 self.d[c].insert(word[i+1:])
#             else:
#                 self.d[c] = Trie()
#                 self.d[c].insert(word[i+1:])
                

#     def search(self, word: str) -> bool:
        
#         if len(word) == 1:
#             c = word[0]
#             if c in self.d:
#                 if self.d[c].is_word:
#                     return True
#                 else:
#                     return False
        
#         for i in range(len(word)-1):
            
#             c = word[i]
            
#             if c in self.d:
#                 print(c)
#                 print(self.d)
#                 print('----------')
#                 return self.d[c].search(word[i+1:])
#             else:
#                 return False
        

#     def startsWith(self, prefix: str) -> bool:
        
#         if len(prefix) == 1:
            
#             c = prefix[0]
            
#             if c in self.d:
#                 return True
#             else:
#                 return False
            
        
#         for i in range(len(prefix)-1):
            
#             c = prefix[i]
            
#             if c in self.d:
#                 print(c)
#                 print(self.d)
#                 print('----------')
#                 return self.d[c].startsWith(prefix[i+1:])
#             else:
#                 return False
            


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
