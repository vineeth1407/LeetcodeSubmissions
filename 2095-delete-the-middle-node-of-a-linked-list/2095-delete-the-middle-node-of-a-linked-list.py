# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sp = head
        fp = head
        prev = None
        
        while fp and fp.next:
             prev = sp
             sp = sp.next
             fp = fp.next.next
             
        if prev:
            prev.next = sp.next
            return head
        return None
        