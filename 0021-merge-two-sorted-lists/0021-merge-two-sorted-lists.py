# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return ans1(list1, list2)
    
def ans1(list1, list2):
    
    start = pt = ListNode(0)

    while list1 and list2:

        a = list1.val
        b = list2.val

        if a <= b:
            pt.next = list1
            list1 = list1.next

        if b < a:
            pt.next = list2
            list2 = list2.next
        
        pt = pt.next
        
    if list1:
        pt.next = list1
    elif list2:
        pt.next = list2
        
    return start.next
            
            
            
        
    
        
        