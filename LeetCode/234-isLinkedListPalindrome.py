# https://leetcode.com/problems/palindrome-linked-list/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return (str(self.val))


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


def generateLinkedList(input: list):
    head = ListNode(input[0])

    currentNode = head
    for value in input[1:]:
        newNode = ListNode(value)
        currentNode.next = newNode
        currentNode = newNode

    return head


def printLinkedList(head: ListNode):
    result = '['

    currentNode = head
    while currentNode:
        result += str(currentNode.val) + ', '
        currentNode = currentNode.next

    print(result[:-2] + ']')


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
        head = generateLinkedList(input)
        print(solution.isPalindrome(head))
