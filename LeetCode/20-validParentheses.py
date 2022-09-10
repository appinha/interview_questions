class Solution:
    def isValid(self, s: str) -> bool:
        openByClosed = {')': '(', ']': '[', '}': '{'}

        stack = []
        for c in s:
            if c in openByClosed.values():
                stack.append(c)
            else:
                if not stack:
                    return False
                pop = stack.pop()
                if pop != openByClosed[c]:
                    return False

        return not stack


if __name__ == '__main__':
    solution = Solution()
    inputs = [
        "()",  # True
        "()[]{}",  # True
        "(]",  # False
        "]",  # False
        "[",  # False
    ]
    for input in inputs:
        print(solution.isValid(input))