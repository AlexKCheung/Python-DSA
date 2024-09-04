# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    output = head
    while head and head.next:
        if head.val == head.next.val:
            head.next = head.next.next
        else:
            head = head.next
    return output