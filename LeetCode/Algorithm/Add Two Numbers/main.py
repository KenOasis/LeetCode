# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1,list2 = [],[]
        while l1 != None:
            list1.append(l1.val)
            l1 = l1.next
        while l2 != None:
            list2.append(l2.val)
            l2 = l2.next
        list1.reverse()
        list2.reverse()
        num1, num2 = 0, 0
        for digit in list1:
            num1 = num1*10 + digit
        for digit in list2:
            num2 = num2*10 + digit
        result_num_reverse = num1 + num2
        list_result = list(str(result_num_reverse))
        next = None
        current = []
        for digit in list_result:
            current_object = ListNode(int(digit), next)
            next = current_object
            current.append(current_object)
        return current[-1]
        
l1_3 =ListNode(3)
l1_2 =ListNode(4,l1_3)
l1 = ListNode(2,l1_2)

l2_3 = ListNode(4)
l2_2 = ListNode(6, l2_3)
l2 = ListNode(5, l2_2)

s = Solution()
k = s.addTwoNumbers(l1,l2)
print(k.next.next.val)
print('test finish')