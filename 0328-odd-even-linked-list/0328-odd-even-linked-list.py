# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head
        
        odd = ListNode()
        even = ListNode()
        even_head = even
        odd_head = odd
        c = 1
        
        while head:
            if c%2==1:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            c+=1
            prev = head
            head = head.next
            prev.next = None
      
        odd.next = even_head.next
        return odd_head.next
        
        