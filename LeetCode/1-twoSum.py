# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementByNum = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complementByNum:
                return [nums.index(complement), i]
            complementByNum[num] = complement


if __name__ == '__main__':
    solution = Solution()
    inputs = [
        [[2,7,11,15], 9],  # [0, 1]
        [[3,2,4], 6],  # [1,2]
        [[3,3], 6],  # [0,1]
        [[-3,4,3,90], 0],  # [0, 2]
    ]
    for input in inputs:
        print(solution.twoSum(*input))