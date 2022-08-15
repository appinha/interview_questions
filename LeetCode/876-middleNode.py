# https://leetcode.com/problems/middle-of-the-linked-list/

from typing import Optional
from helpers import ListNode, LinkedList


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len = LinkedList.len(head)
        return head[len // 2]


if __name__ == '__main__':
    solution = Solution()
    inputs = [
        [1],
        [1, 2],
        [1, 2, 3, 4],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6],
    ]
    for input in inputs:
        head = LinkedList.generate(input)
        print(solution.middleNode(head))
