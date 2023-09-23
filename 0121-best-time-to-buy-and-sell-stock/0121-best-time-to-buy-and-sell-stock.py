'''
[7,1,5,3,6,4]
[7,6,4,3,1]
[2,1,2,1,0,1,2]
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return p2(prices)
    
'''One Pass Two-Pointer Approach'''
def ans_1(prices: List[int]) -> int:

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