# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        if not head:
            return head
        prev = None
        while head:
            t= head.next
            head.next = prev
            prev = head
            head = t
        return prev
    
    def pairSum(self, head: Optional[ListNode]) -> int:
        sp = head
        fp = head
        max_sum = 0
        
        if not fp.next.next:
            return fp.val + fp.next.val
        while fp and fp.next:
            fp = fp.next.next
            sp = sp.next
        
        print(sp.val)
        rev = self.reverse(sp)
        
        while rev and head:
            cur_sum = rev.val + head.val
            max_sum = max(max_sum,cur_sum)
            rev=rev.next
            head=head.next
        return max_sum
            
        
        