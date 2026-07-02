class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        
        temp=head
        count=0
        
        while temp is not None:
            count+=1
            temp=temp.next

        remaining_traversal=count-n 
        temp=head
        prev=None

        for i in range(remaining_traversal):
            prev=temp
            temp=temp.next
            
        if prev is None:
            return head.next

        prev.next=temp.next
        return head
