class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
         s=head
         f=head
         for i in range(0,n):
            f=f.next

         while f is not None and  f.next is not None:
            s=s.next
            f=f.next
         if f is None:
             return s.next
         else:
           s.next=s.next.next
         return head