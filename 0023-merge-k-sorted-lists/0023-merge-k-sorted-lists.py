# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq as hp

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return ans1(lists)

def recur(nums):
    # print(nums)
    if nums == []:
        return None
    
    val = hp.heappop(nums)
    return ListNode(val, recur(nums))

def ans1(lists):
    
    a = []
    
    for node in lists:
        while node:
            a.append(node.val)
            node = node.next
    
    # print(a)
    
    if a == []:
        # return ListNode()
        return
    
    hp.heapify(a)
    # print(a)
    
    z = recur(a)
    return z
    
    # for n in a:
    #     m = hp.heappop(a)
    #     x = ListNode(m, None)
    #     las
    
    
    # print(lists[0])
    # print(type(lists[0]))
    # x = lists[0]
    # print(x.val)
    # print(x.next.val)
    # print(x.next.next.val)