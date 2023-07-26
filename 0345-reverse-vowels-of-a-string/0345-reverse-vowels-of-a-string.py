from collections import deque

class Solution:
    def reverseVowels(self, s: str) -> str:
        return ans1(s)
    
def ans1(s):
    
    vowels = 'aeiouAEIOU'
    l = len(s)
    
    found = deque()
    ans = ''
    
    for letter in s:
        if letter in vowels:
            found.append(letter)
    
    for letter in s:
        if letter in vowels:
            ans += found.pop()
        else:
            ans += letter
    
    return ans
        
        