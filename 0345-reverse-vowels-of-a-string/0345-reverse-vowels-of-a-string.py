'''
"hello"
"leetcode"
'''

from collections import deque

class Solution:
    def reverseVowels(self, s: str) -> str:
        return ans1(s)
    


'''
TC = n, 
SC = n
Worst case is if all the letters are vowels, then
1. the stack will have all n letters
2. and the ans string takes n iterations to be made anyway

'''
def ans1(s):
    
    vowels = 'aeiouAEIOU'
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
        
        