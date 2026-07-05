# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        prev=head
        temp=head.next

        while temp:
            if prev.val!=temp.val:
                prev.next=temp
                prev=temp
            temp=temp.next
            prev.next=temp
        return head