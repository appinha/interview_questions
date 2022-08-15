# https://leetcode.com/problems/palindrome-linked-list/

from typing import Optional
from helpers import ListNode, LinkedList


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        allValues = []
        currentNode = head
        while currentNode:
            allValues.append(currentNode.val)
            currentNode = currentNode.next

        for i, value in enumerate(reversed(allValues)):
            if allValues[i] != value:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    inputs = [
        [1],
        [2, 2],
        [1, 2, 2, 1],
        [1, 2, 3, 2, 1],
        [1, 2, 3, 1],
    ]
    for input in inputs:
        head = LinkedList.generate(input)
        print(solution.isPalindrome(head))
