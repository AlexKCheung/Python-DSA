# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
    nums = set(nums)
    while head:
        if head.val not in nums:
            res = head
            break
        head = head.next

    output = res
    while res and res.next:
        if res.next.val in nums:
            res.next = res.next.next
        else:
            res = res.next
    return output
