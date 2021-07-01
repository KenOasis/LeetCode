# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
        Do it step by step and consider all the endpoint (when result returned)
        consider the most normal situation before the extreme one 
    """
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        result_current = result.next
        l1_current = l1
        l2_current = l2
        while l1_current != None or l2_current != None:
            if l1_current != None and l2_current == None:
                if result.next == None:
                    result.next = l1_current
                else:
                    result_current.next = l1_current
                return result.next
            elif l1_current == None and l2_current != None:
                if result.next == None:
                    result.next = l2_current
                else:
                    result_current.next = l2_current
                return result.next
            else:
                if l1_current.val <= l2_current.val:
                    if result.next == None:
                        result.next = l1_current
                        result_current = result.next
                    else:
                        result_current.next = l1_current
                        result_current = result_current.next
                    l1_current = l1_current.next
                else:
                    if result.next == None:
                        result.next = l2_current
                        result_current = result.next
                    else:
                        result_current.next = l2_current
                        result_current = result_current.next
                    l2_current = l2_current.next
        return result.next 