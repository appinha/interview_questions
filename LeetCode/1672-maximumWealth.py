# https://leetcode.com/problems/richest-customer-wealth/

from typing import List
from collections import defaultdict


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealthByCustomer = defaultdict(int)
        for i, row in enumerate(accounts):
            for j in row:
                wealthByCustomer[i] += j
        return max(wealthByCustomer.values())


if __name__ == '__main__':
    solution = Solution()
    inputs = [
        [[1,2,3],[3,2,1]],  # 6
        [[1,5],[7,3],[3,5]],  # 10
        [[2,8,7],[7,1,3],[1,9,5]],  # 17
    ]
    for input in inputs:
        print(solution.maximumWealth(input))