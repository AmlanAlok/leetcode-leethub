class Solution:
    def isPalindrome(self, s: str) -> bool:
        return p2(s)
        
    def ans1(self, s: str) -> bool:

        if len(s)==0:
            return False
        
        p=''
        
        for i in s:
            if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90) or (ord(i)>=48 and ord(i)<=57):
                print(ord(i))
                p=p+i
        
        print(p)
        
        p = p.lower()
        print(p)
        
        if len(p)==1:
            if p[0].isalpha():
                return True
            else:
                return False
        
        i, j = 0, len(p)-1

        while i<=j:
            
            if p[i] != p[j]:
                
                return False
            
            i+=1
            j-=1
            
        return True
    '''
    Two pointer
    TC = n
    SC = 1
    '''
    def ans2(self, s: str) -> bool:
        
        i, j = 0, len(s)-1
        
        while i<j:
            
            while i<j and not s[i].isalnum():
                i+=1
            while i<j and not s[j].isalnum():
                j-=1
            
            if s[i].lower() != s[j].lower():
                return False
            
            i+=1
            j-=1
            
        return True
    
    '''
    TC = n
    SC = n
    '''
    def ans3(self, s: str) -> bool:
        
        f = ''
        
        for c in s:
            if ord(c) >= 65 and ord(c) <=90:
                f += chr(ord(c) + 32)
            if ord(c) >= 97 and ord(c) <=122 or ord(c) >= 48 and ord(c) <=57:
                f += c
            
        rev = f[::-1]
        
        # print(rev)
        # print(f)
        return rev == f
    
    '''
    Two pointer
    TC = n
    SC = 1
    '''
    def p1(self, s: str) -> bool:
        
        i, j = 0, len(s)-1
        
        while i<j:
            
            while i<j and not s[i].isalnum():
                i += 1
            while i<j and not s[j].isalnum():
                j -= 1
            
            if s[i].lower() != s[j].lower():
                return False
            
            i+=1
            j-=1
            
        return True
        
    
def p2(s):
    
    i,j = 0, len(s)-1
    
    while i < j:
        
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        
        if s[i].lower() != s[j].lower():
            return False
        
        i += 1
        j -= 1
    
    return True
            
    
    
        
        
        
        
        
        
           
           