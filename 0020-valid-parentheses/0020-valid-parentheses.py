'''
"()"
"()[]{}"
"(]"
'''
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        return dec02(s)
    
    def ans1(self, s: str) -> bool:
        
        a=deque()
        
        for v in s:
            
            if a:
                if v==')' and a[-1] == '(' or v=='}' and a[-1]=='{' or v == ']' and a[-1]=='[':
                    a.pop()
                    continue
            
            a.append(v)
            
        return len(a)==0
    
    def p1(self, s: str) -> bool:
        
        a = []
        
        for i in s:
            
            if a:
                if (i == '}' and a[-1] == '{') or (i == ')' and a[-1] == '(') or (i == ']' and a[-1] == '['):
                    a.pop()
                    continue
            
            a.append(i)
        
        return len(a)==0

    def p2(self, s: str) -> bool:
        
        a = []
        
        for i in range(len(s)):

            x = s[i]
            
            if a:
                if (x==')' and a[-1]=='(') or (x=='}' and a[-1]=='{') or (x==']' and a[-1]=='['): 
                    a.pop()
                    continue
                
            a.append(x)
            
        return len(a)==0
            
def oct22(s):
    st = deque()
    
    for c in s:
        
        if st:
            
            x = c == ')' and st[-1] == '('
            y = c == '}' and st[-1] == '{'
            z = c == ']' and st[-1] == '['
            
            if x or y or z:
                st.pop()
                continue
        
        st.append(c)
    
    return len(st) == 0

def dec02(s):
    
    st = deque()
    
    for c in s:
        
        if st:
            if (c == ')' and st[-1] == '(') \
            or (c == '}' and st[-1] =='{') \
            or (c == ']' and st[-1] == '['):
                st.pop()
                continue
            
        st.append(c)
    
    return len(st) == 0

    
    
        