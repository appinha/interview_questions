# https://leetcode.com/problems/merge-two-sorted-lists/submissions/

from typing import Optional
from helpers import ListNode, LinkedList


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            mergedList = list1
            list1 = list1.next
        else:
            mergedList = list2
            list2 = list2.next

        currM = mergedList
        while True:
            if not list1 and not list2:
                break
            if not list1:
                currM.next = list2
                break
            if not list2:
                currM.next = list1
                break
            if  list1.val <= list2.val:
                currM.next = list1
                currM = currM.next
                list1 = list1.next
            else:
                currM.next = list2
                currM = currM.next
                list2 = list2.next

        return mergedList


if __name__ == '__main__':
    solution = Solution()
    inputs = [
        [None, None],
        [[1], None],
        [None, [1]],
        [[1], [2]],
        [[1], [2, 3]],
        [[1, 2, 3], [2, 3]],
    ]
    for input in inputs:
        list1 = LinkedList.generate(input[0]) if input[0] else input[0]
        list2 = LinkedList.generate(input[1]) if input[1] else input[1]
        LinkedList.print(solution.mergeTwoLists(list1, list2))