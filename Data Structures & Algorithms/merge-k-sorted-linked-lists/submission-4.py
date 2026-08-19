# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        index = len(lists)

        if index == 0:
            return None

        while index > 1:
            end = index-1
            index = 0
            for i in range(0, end, 2):
                curr_node = lists[i]
                curr_mrg = lists[i+1]
                dummy = ListNode()
                curr_dummy = dummy
                while curr_node and curr_mrg:
                    if curr_node.val < curr_mrg.val:
                        curr_dummy.next = curr_node
                        curr_node = curr_node.next
                    else:
                        curr_dummy.next = curr_mrg
                        curr_mrg = curr_mrg.next
                    curr_dummy = curr_dummy.next

                if curr_node is not None:
                    curr_dummy.next = curr_node
                
                if curr_mrg is not None:
                    curr_dummy.next = curr_mrg
                
                lists[index] = dummy.next
                index+=1

            if end % 2 == 0:
                lists[index] = lists[end]
                index += 1
        
        return lists[0]