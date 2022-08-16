# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num -= 1
            steps += 1
        return steps


if __name__ == '__main__':
    solution = Solution()
    inputs = [
        14,  # 6
        8,  # 4
        123,  # 12
    ]
    for input in inputs:
        print(solution.numberOfSteps(input))