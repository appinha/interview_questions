# https://leetcode.com/problems/palindrome-linked-list/

from typing import Optional
from helpers import ListNode, LinkedList


class Solution:
    # O(n) time and space
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        allValues = []
        currentNode = head
        while currentNode:
            allValues.append(currentNode.val)
            currentNode = currentNode.next
        return allValues == allValues[::-1]

    # O(n) time and O(1) space
    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        length = LinkedList.len(head)
        if length == 1:
            return True
        halfLength = length // 2
        hasMiddleNode = length % 2 != 0

        i = 1
        j = halfLength
        halfSum = 0
        currentNode = head
        while currentNode:
            if hasMiddleNode and i == halfLength + 1:
                pass
            elif i <= halfLength:
                halfSum += currentNode.val * (i + 1)
            else:
                halfSum -= currentNode.val * (j + 1)
                j -= 1
            i += 1
            currentNode = currentNode.next

        return halfSum == 0


if __name__ == '__main__':
    solution = Solution()
    inputs = [
        [1],  # True
        [2, 2],  # True
        [1, 2, 2, 1],  # True
        [1, 2, 3, 2, 1],  # True
        [1, 3, 2, 4, 3, 2, 1],  # False
        [1, 2, 3, 1],  # False
    ]
    for input in inputs:
        head = LinkedList.generate(input)
        print(solution.isPalindrome(head), solution.isPalindrome2(head))
