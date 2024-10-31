# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    temp = None
    cur = head
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev
        