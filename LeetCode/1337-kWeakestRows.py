# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

from typing import List
from collections import defaultdict
from pprint import pprint


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        indexesBySum = defaultdict(list)
        for i, row in enumerate(mat):
            indexesBySum[sum(row)].append(i)

        orderedRows = []
        for s in sorted(indexesBySum):
            orderedRows += indexesBySum[s]

        return orderedRows[:k]


if __name__ == '__main__':
    solution = Solution()
    inputs = [
        [[[1,1,0,0,0],
          [1,1,1,1,0],
          [1,0,0,0,0],
          [1,1,0,0,0],
          [1,1,1,1,1]], 3],
        [[[1,0,0,0],
          [1,1,1,1],
          [1,0,0,0],
          [1,0,0,0]], 2],
    ]
    for input in inputs:
        print(solution.kWeakestRows(*input))
