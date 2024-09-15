# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]
    mid = len(lists) // 2
    left = self.mergeKLists(lists[:mid])
    right = self.mergeKLists(lists[mid:])
    return self.mergeList(left, right)

def mergeList(self, list1, list2):
    cur = head = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next
    if list1:
        cur.next = list1
    if list2:
        cur.next = list2
    return head.next