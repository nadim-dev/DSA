# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        temp=head
        while temp is not None:
            count+=1
            temp=temp.next
        temp=head

        for i in range(0,count//2):
            temp=temp.next
        return temp




        