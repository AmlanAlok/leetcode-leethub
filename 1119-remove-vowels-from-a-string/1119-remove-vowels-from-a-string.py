class Solution:
    def removeVowels(self, s: str) -> str:
        return ans1(s)
    
def ans1(s):
    
    vowels = 'aeiouAEIOU'
    
    ans = ''
    
    for v in s:
        if v not in vowels:
            ans += v
    return ans