# https://leetcode.com/problems/merge-two-sorted-lists/?envType=featured-list&envId=top-interview-questions


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def solution(self, list1, list2, newList):
        if list1 is None and list2 is None:
            return newList
        elif list1 is None:
            newList.val = list2.val
            newList.next = ListNode()
            return self.solution(list1, list2.next, newList.next)
        elif list2 is None:
            newList.val = list1.val
            newList.next = ListNode()
            return self.solution(list1.next, list2, newList.next)
        elif list1.val <= list2.val:
            newList.val = list1.val
            newList.next = ListNode()
            return self.solution(list1.next, list2, newList.next)
        else:
            newList.val = list2.val
            newList.next = ListNode()
            return self.solution(list1, list2.next, newList.next)


    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = None
        self.solution(list1, list2, head)
        return head
