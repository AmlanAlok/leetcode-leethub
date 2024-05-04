'''
[7,1,5,3,6,4]
[7,6,4,3,1]
[2,1,2,1,0,1,2]
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return may05_24(prices)
    

def ans_1(prices: List[int]) -> int:
    '''One Pass Two-Pointer Approach'''
    b = 0
    s = 0
    m = 0

    for i in range(1, len(prices)):

        p = prices[i] - prices[b]

        if p > 0:
            if p > m:
                m = p

        if p < 0:
            b = i

    return m

def p1(prices: List[int]) -> int:

    nums = prices
    m=0
    b=0
    s=0

    for i in range(len(prices)):

        p = nums[i]-nums[b]

        if p > 0 and p > m:
                m=p
        if p<0:
            b=i

    return m

def p2(prices: List[int]) -> int:
    i, j = 0, 0
    mx = 0

    while i < len(prices) and j < len(prices):

        p = prices[j]-prices[i]

        if p > mx:
            mx = p
        if p < 0:
            i = j
        j += 1

    return mx

def may05_24(prices):
    
    buy = prices[0]
    sell = 0
    profit = 0
    
    for sell in prices:
        if sell < buy:
            buy = sell
        
        profit = max(sell - buy, profit)
    
    return profit 


def may04_24(prices):
    
    buy = prices[0]
    sell = 0
    profit = 0
    
    for n in prices:
        if n < buy:
            buy = n
            sell = n
        if n > sell:
            sell = n
        
        profit = max(sell - buy, profit)
    
    return profit 
        
    
    