'''
"the sky is blue"
"a good   example"
"  hello world  "
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        return self.ans2(s)
    
    def ans2(self, s: str) -> str:
        s = s.strip()
        
        s = s.split()
        print(s)
        t = []
        
        # for x in s:
        #     if x != '':
        #         t.append(x)
        
        return ' '.join(s[::-1])
        
    def ans1(self, s: str) -> str:
        
        s = s.strip()
        
        t = []
        x = ''
        for c in s:
            if c == ' ':
                t.append(x)
                x = ''
            else:
                x += c
        t.append(x)
        x = ''
        
        ans = ''
        for i in range(len(t)-1, 0, -1):
            
            a = t[i]
            ans += a
            ans += ' '
        ans += t[0]

        return ans
        
        
        