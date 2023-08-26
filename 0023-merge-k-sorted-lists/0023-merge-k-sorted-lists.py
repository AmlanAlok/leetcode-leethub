# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq as hp

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return ans1(lists)

def recur(nums):        # TC = n as it recurs n times
    # print(nums)
    if nums == []:
        return None
    
    val = hp.heappop(nums)      # TC = log n
    return ListNode(val, recur(nums))

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
def ans2(lists):
    h = []
    head = pt = ListNode(0)
    c = 0
    
    for ll in lists:
        if ll:
            hp.heappush(h, (ll.val, c, ll))
            c += 1
    
    while len(h):
        sm = hp.heappop(h)[2]
        pt.next = sm
        pt = pt.next
        
        if sm.next:
            x = sm.next
            hp.heappush(h, (x.val, c, x))
            c += 1
            
    return head.next
            
    
    
    
    
    
    
    
    
    
    