'''
"internationalization"
"i12iz4n"
"substitution"
"s55n"
"substitution"
"s010n"
"substitution"
"s10n"
"substitution"
"sub4u4n"
"substitution"
"12"
"substitution"
"su3ilu2on"
'''
class Solution:
    def validWordAbbreviation(self , word: str, abbr: str) -> bool:
        return ans(word, abbr)
    
'''
not adjacent
not empty
no leading 0
'''



def ans(word, abbr):
    
    def is_number(c):
        return True if 48 <= ord(c) <= 58 else False

    i = 0
    j = 0
    M, N = len(word), len(abbr)
    
    while j < M and i < N:
        
        if word[j] == abbr[i]:
            i += 1
            j += 1
        elif abbr[i] == '0':
            return False
        elif is_number(abbr[i]):
            k = i
            while k < N and is_number(abbr[k]):
                k += 1
                
            num = int(abbr[i:k])
            i = k
            j += num
        else:
            return False
    
    return i == N and j == M


def fail(word, abbr):
    
    N = len(word)
    M = len(abbr)
    i = 0
    j = 0
    zero = ord('0')
    
    while i < M and j < N:
        
        if word[j] != abbr[i]:
            
            if abbr[i] == zero:
                return False
            
            exp = 0
            num = 0
            
            while i < M and 49 <= ord(abbr[i]) <= 57:
                val = ord(abbr[i]) - zero
                num = (10**exp * num) + val
                i += 1
                exp += 1
            
            if num == 0:
                return False
            
            j = j + num
            
            if j > N:
                return False
        
        else:
            i, j = i + 1, j + 1
        
    return True

'''
"internationalization"
"i12iz4n"
"apple"
"a2e"
"internationalization"
"i5a11o1"
"hi"
"hi1"
'''

def discus(word, abbr):
    i = j = 0
    m, n = len(word), len(abbr)
    while i < m and j < n:
        if word[i] == abbr[j]:
            i += 1
            j += 1
        elif abbr[j] == "0":
            return False
        elif abbr[j].isnumeric():
            k = j
            while k < n and abbr[k].isnumeric():
                k += 1
            i += int(abbr[j:k])
            j = k
        else:
            return False
    return i == m and j == n
        
            
            
            
            
            
            
                
            
    
    
    
    
    
    
    
    
    
    