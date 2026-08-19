# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ln = 0
        curr = head

        while curr:
            ln+=1
            curr = curr.next
        
        if ln < k:
            return head

        curr = head
        prev = None
        tail = head
        new_tail = head
        counter = 0

        while curr:
            counter += 1
            next_node = curr.next
            curr.next = prev
            prev = curr
            
            if counter % k == 0:
                if counter // k == 1:
                    head = prev
                
                tail.next = prev
                tail = new_tail
                prev = None
                new_tail = next_node

                if counter+k > ln:
                    tail.next = next_node
                    break

            curr = next_node

        return head
