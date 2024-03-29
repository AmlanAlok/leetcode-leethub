'''
https://leetcode.com/problems/longest-repeating-character-replacement/discuss/4443411/Explaining-intuition-behind-why-lowering-the-max_frequency-is-not-required

"ABAB"
2
"AABABBA"
1
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # return p(s, k)
        return p(s, k)
        
    
def ans1(s, k):
    d = {}
    l = r = 0
    
    res = 0
    
    # while l < len(s) and r < len(s):
    for r in range(len(s)):
        
        d[s[r]] = d.get(s[r], 0) + 1
        
        # max(d.values()) is TC = O(26)
        while (r-l+1) - max(d.values()) > k:
            d[s[l]] -= 1
            l += 1
        
        res = max(res, (r-l+1))
        
        r += 1
    
    return res

def ans2(s, k):
    '''
    The intuition for this ans is very important.
    You need to find the longest substring.
    Longest is the key hint.
    When maxf is maximum, the window length is maximum.
    So maxf value decreases later, the valid window length will also decrese, but we only care about the max window length. 
    So for mathematically covering all the scenarios and then finding the max window length, changing the maxf to lower it is important.
    But if you only want the longest window length, then you only care about the maxf scenario. So you just increase maxf value in every iteration. 
    The ans for longest substring will come when maxf is maximum. For anything not max value, the window length will also be lower which we do not care about.
    So you can skip unnecessary calculations.
    '''
    
    d = {}
    l = r = 0
    
    res = 0
    maxf = 0
    
    # while l < len(s) and r < len(s):
    for r in range(len(s)):
        
        d[s[r]] = d.get(s[r], 0) + 1
        maxf = max(maxf, d[s[r]])
        
        # max(d.values()) is TC = O(26)
        while (r-l+1) - maxf > k:
            d[s[l]] -= 1
            l += 1
        
        res = max(res, (r-l+1))
        
        # r += 1
    
    return res

def dec21(s, k):
    
    i = j = 0
    d = {}
    mx = 0
    
    for j in range(len(s)):
        c = s[j]
        
        d[c] = d.get(c, 0) + 1
        
        if (j-i+1) - max(d.values()) > k:
            z = s[i]
            d[z] -= 1
            i += 1
        
        mx = max(mx, (j-i+1))
    
    return mx
    
def dec22(s, k):
    
    i = j = 0
    d = {}
    mx = 0
    maxf = 0
    
    for j in range(len(s)):
        c = s[j]
        d[c] = d.get(c, 0) + 1
        maxf = max(maxf, d[c])
        
        while (j-i+1) - maxf > k:
            z = s[i]
            d[z] -= 1
            i += 1
        
        mx = max(mx, (j-i+1))
    
    return mx

'''Does not work'''
def jan26(s, k):
    '''TC = 2n = n, SC = 26'''
    n = len(s)
    mx = 0
    d = {}
    maxf = 0
    i = 0
    j = 0
    
    while j < n:
        
        while (j-i+1) - maxf <= k and j < n:
            c = s[j]
            d[c] = d.get(c, 0) + 1
            
            if d[c] > maxf:
                maxf = d[c]
            
            if (j-i+1) > mx and (j-i+1) - maxf <= k:
                mx = (j-i+1)
            
            j += 1
        
        while (j-i+1) - maxf > k and i < j:
            c = s[i]
            d[c] -= 1
            i += 1
            # if d[c] == 0:
            #     del d[c]    # this will optimize space to k+1
            
    return mx

def p(s, k):
    
    n = len(s)
    mx = 0
    i = 0
    d = {}
    maxf = 0
    
    for j in range(n):
        c = s[j]
        d[c] = d.get(c, 0) + 1
        if d[c] > maxf:
            maxf = d[c]
        
        while (j-i+1) - maxf > k:
            z = s[i]
            d[z] -= 1
            i += 1
        
        length = (j-i+1)
        
        if length > mx:
            mx = length
    
    return mx
        
def prac(s, k):

	max_len = 0
	i = j = 0
	n = len(s)
	dict = {}
	max_freq = 0

	while j < n:
		c = s[j]
		dict[c] = dict.get(c, 0) + 1

		max_freq = max(max_freq, dict[c])

		if (j-i+1) - max_freq <= k:
			max_len += 1
		else:
			i = j - max_len
			c = s[i]
			dict[c] -= 1

			if dict[c] == 0:
				del dict[c]

		j += 1

	return max_len