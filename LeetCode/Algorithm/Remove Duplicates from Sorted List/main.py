# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current_node = head
        while current_node != None and current_node.next != None:
            next_node = current_node.next
            while current_node != None and next_node != None and current_node.val == next_node.val:
                current_node.next = next_node.next
                next_node = next_node.next
            current_node = current_node.next
        return head
