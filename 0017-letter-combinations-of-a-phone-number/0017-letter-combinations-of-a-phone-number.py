'''
"23"
""
"2"
"6789"
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        return ans1(digits)

d = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}    

def ans1(digits):
    
    if digits == '':
        return []
    
    x = digits[0]
    letters = d[x]
    
    new_digits = digits[1:]
    
    v = ans1(new_digits)
    
    if len(v) == 0:
        for c in letters:    
            v.append(c)
        return v
    else:
        ans = []
        for c in letters:
            for k in v:
                ans.append(c+k)
        return ans

        
        