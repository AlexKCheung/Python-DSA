# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    temp = merged_list = ListNode()
    while list1 and list2: 
        if list1.val < list2.val: 
            merged_list.next = list1
            list1 = list1.next
        else: 
            merged_list.next = list2
            list2 = list2.next
        merged_list = merged_list.next
        
    if list1: 
        merged_list.next = list1
    if list2: 
        merged_list.next = list2
    
    return temp.next