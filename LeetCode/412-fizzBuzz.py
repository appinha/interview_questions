# https://leetcode.com/problems/fizz-buzz/

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range (1, n + 1):
            output = str(i)
            if i % 3 == 0 and i % 5 == 0:
                output = "FizzBuzz"
            elif i % 3 == 0:
                output = "Fizz"
            elif i % 5 == 0:
                output = "Buzz"
            answer.append(output)
        return answer


if __name__ == '__main__':
    solution = Solution()
    inputs = [3, 5, 15]
    for input in inputs:
        print(solution.fizzBuzz(input))
