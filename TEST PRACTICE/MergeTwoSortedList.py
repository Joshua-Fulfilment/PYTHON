#Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

class Solution:
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode] 
        :rtype: Optional[ListNode]:
        """

        if not list1: return list2
        if not list2: return list1

        dummy = prev = ListNode(-1)
        dummy.next = list1
        n1 = list1
        n2 = list2

        while n1 and n2:
            if n2.val > n1.val:
                if not n1.next: n1.next= n2; break
                prev= n1
                n1 = n1.next
            else:
                temp = n2.next
                prev.next = n2
                n2.next = n1
                prev = n2
                n2 = temp
        
        return dummy.next 