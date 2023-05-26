'''
Test case
"/home/"
"/../"
"/home//foo/"
"/a/./b/../../c/"
'''
class Solution:
    
    def simplifyPath(self, path: str) -> str:
        return ans3(path)
    
'''Using list'''
def ans4(path):
    from collections import deque
        
    parts = path.split('/')
    
    s = []
    
    for p in parts:
        if p == '..':
            if s:
                s.pop()
        elif p in {'.', ''}:
            continue
        else:
            s.append(p)

    return '/' + '/'.join(s)

'''TC = O(n), SC = O(2n)'''
def ans3(path):
    from collections import deque
        
    parts = path.split('/')
    
    s = deque()
    
    for p in parts:
        if p == '..':
            if s:
                s.pop()
        elif p in {'.', ''}:
            continue
        else:
            s.append(p)

    return '/' + '/'.join(s)
        
def fail1(path: str) -> str:
        
        s = path
        
        s = s.replace('//','/')
        s = s.replace('.','')
        
        if s[0] != '/':
            s = '/'+s
        
        if s[-1] == '/':
            s = s[:-1]
            
        return s
        
def ans1(path: str) -> str:
        
        from collections import deque
        
        s = deque()
        p = path
        
        p = p.split('/')
        
        print(p)
        
        for i, v in enumerate(p):

            if v == '..' and s:
                s.pop()
                
            elif v == '.' or v == '' or v == '..':
                continue
            
            elif isinstance(v, str):
                s.append(v)
            
        print(s)
                
        return '/'+'/'.join(s)
            
def ans2(path):
    from collections import deque
        
    path = path.replace('//', '/')
    parts = path.split('/')
    
    s = deque()
    
    for p in parts:
        if p == '..':
            if len(s) > 0:
                s.pop()
            continue
        if p == '.':
            continue
        if p is not '':
            s.append(p)
    
    ans = ''
    
    for st in s:
        ans += '/' + st
    
    if ans is '':
        return '/'
    return ans
    
    
            
            
    
        