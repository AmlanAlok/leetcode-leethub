'''
"ABCABC"
"ABC"
"ABABAB"
"ABAB"
"LEET"
"CODE"
"TAUXXTAUXXTAUXXTAUXXTAUXX"
"TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
"ABABABAB"
"ABAB"
'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        return ans2(str1, str2)
    
def ans2(s1, s2):
    if len(s2) > len(s1):
        s1, s2 = s2, s1

    n, m = len(s1), len(s2)

    for j in range(m, 0, -1):
        r = n % j
        if r == 0:
            base = s2[0:j]
            
            p, q = n // j, m//j
            
            if p*base == s1 and q*base == s2:
                return base
    return ''
    
'''My attempt'''
def ans1(s1, s2):

    if len(s2) > len(s1):
        s1, s2 = s2, s1

    n, m = len(s1), len(s2)

    for j in range(m, 0, -1):

        r = n % j

        if r == 0:
            # print(r)
            d = int(n/j)
            start, end = 0, j
            
            base = s2[0:j]
            
            p, q = n // j, m//j
            
            if p*base == s1 and q*base == s2:
                return base
            
            # for k in range(1, d+1):
            #     print(s2[0:j], s1[start:end])
            #     if s2[0:j] != s1[start:end]:
            #         break
            #     if k == d:
            #         return s2[0:j]
            #     start += j
            #     end += j
    
    return ''
            
                
                
        
        
        
        
        