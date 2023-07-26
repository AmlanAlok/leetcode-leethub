'''
"hello"
"leetcode"

".,"
'''

from collections import deque

class Solution:
    def reverseVowels(self, s: str) -> str:
        # return ans1(s)
        return ans2(s)
    

def ans2(s):
    vowels = 'aeiouAEIOU'
    l = len(s)
    i, j = 0, len(s)-1
    
    st = list(s)
    
    while i < j:

        while i < l and st[i] not in vowels:
            i += 1
        while j >= 0 and st[j] not in vowels:
            j -= 1
        
        if i<j:
            st[i], st[j] = st[j], st[i]
            i += 1
            j -= 1
        else:
            break

    
    return ''.join(st)
    

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
        
        