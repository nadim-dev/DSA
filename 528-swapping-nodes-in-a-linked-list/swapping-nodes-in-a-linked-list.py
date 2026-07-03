class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
         s=head
         f=head
         count=0
         for _ in range(0,k):
            count+=1
            if count==k:
                i=f
            f=f.next
         while f is not None:
             s=s.next
             f=f.next
         i.val,s.val=s.val,i.val
         return head