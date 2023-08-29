# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq as hp

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return p1(lists)

def recur(nums):        # TC = n as it recurs n times
    # print(nums)
    if nums == []:
        return None
    
    val = hp.heappop(nums)      # TC = log n
    return ListNode(val, recur(nums))

'''n log(n)'''
def ans1(lists):
    
    a = []
    
    for node in lists:      # TC = k
        while node:         # TC = n
            a.append(node.val)
            node = node.next
    
    if a == []:
        return
    
    hp.heapify(a)           # TC = n
    
    z = recur(a)            # TC = n log n
    return z

# https://medium.com/tech-life-fun/leetcode-23-merge-k-sorted-lists-graphically-explained-python3-solution-d0e77419956c
'''TC = n log(k)'''
def ans2(lists):
    h = []
    head = pt = ListNode(0)
    c = 0
    
    for ll in lists:        # TC = k
        if ll:
            hp.heappush(h, (ll.val, c, ll))
            c += 1
    
    while len(h):           # TC = n
        sm = hp.heappop(h)[2]       # TC = log k
        pt.next = sm
        pt = pt.next
        
        if sm.next:
            x = sm.next
            hp.heappush(h, (x.val, c, x))       # TC = log k
            c += 1
            
    return head.next
                
    
def p1(lists):
    
    start = pt = ListNode(0)
    h = []
    c = 0
    for ll in lists:
        if ll:
            hp.heappush(h, (ll.val, c, ll))
            c+=1
    
    while len(h) > 0:
        mini = hp.heappop(h)[2]
        pt.next = mini
        pt = pt.next
        
        if mini.next:
            x = mini.next
            hp.heappush(h, (x.val, c, x))
            c+=1
    
    return start.next
        
    
    
    
    
    
    