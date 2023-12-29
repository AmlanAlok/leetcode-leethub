'''
[1,2,4]
[1,3,4]
[]
[]
[]
[0]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return dec28(list1, list2)
    
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
            
def dec28(list1, list2):
    
    start = end = ListNode()
    
    while list1 and list2:
        
        if list1.val <= list2.val:
            end.next = list1
            list1 = list1.next
        elif list2.val < list1.val:
            end.next = list2
            list2 = list2.next
        
        end = end.next
            
    if list1:
        end.next = list1
        
    elif list2:
        end.next = list2
        
    return start.next


        