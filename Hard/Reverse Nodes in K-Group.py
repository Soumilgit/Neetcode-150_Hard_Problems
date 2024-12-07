# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node, count = head, 0
        while node and count < k: node, count = node.next, count + 1  
        if count < k: return head  
        prev, curr = None, head
        for _ in range(k): curr.next, prev, curr = prev, curr, curr.next 
        head.next = self.reverseKGroup(curr, k) 
        return prev
