# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        visit = set()
        while curr:
            if curr.val not in visit:
                visit.add(curr.val)
            else:
                return True
            curr=curr.next
        else:
            return False
        