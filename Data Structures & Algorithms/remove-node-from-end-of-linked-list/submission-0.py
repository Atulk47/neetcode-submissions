# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        nodes=[]
        while curr:
            nodes.append(curr)
            curr=curr.next
        el_to_rem = len(nodes)-n
        
        if el_to_rem == 0:
            return head.next

        nodes[el_to_rem - 1].next = nodes[el_to_rem].next
        return head
        

        
        