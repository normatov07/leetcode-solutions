# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        left_node = dummy

        for _ in range(left-1):
            left_node = left_node.next

        curr = left_node.next
       
        mid = curr
        prev = None
        for _ in range(right-left+1):
            next_node = curr.next 
            curr.next = prev
            prev = curr
            curr = next_node
        
        left_node.next = prev
        mid.next = curr

        return dummy.next

            
