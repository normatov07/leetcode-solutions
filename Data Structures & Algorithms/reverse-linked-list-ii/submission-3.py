# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        left_node = head
        prev = head
        right -= left

        for _ in range(left-1):
            prev = left_node
            left_node = left_node.next

        curr = left_node.next
        mid = left_node
        while right > 0 and curr:
            tmp = curr.next 
            curr.next = left_node 
            mid.next = tmp
            left_node, curr = curr, mid
            curr = curr.next
            right-=1
        
        if left == 1:
            return left_node
        
        prev.next = left_node

        return head

            
