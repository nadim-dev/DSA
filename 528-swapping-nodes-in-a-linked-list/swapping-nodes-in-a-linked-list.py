# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
         temp=head
         count=0
         if head.next is None:
            return head
         while temp is not None:
            temp=temp.next
            count+=1
         #locating left pointer
         i=head
         for _ in range(0,k-1):
            i=i.next
         #locating rigth pointer
         j=head
         for _ in range(0,count-k):
            j=j.next
         # now swapping occur's
         i.val,j.val=j.val,i.val
         return head

