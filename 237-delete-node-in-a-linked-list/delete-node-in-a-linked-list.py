# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        temp=node
        next_node=temp.next
        temp.val=next_node.val
        temp.next=next_node.next


        

        
        