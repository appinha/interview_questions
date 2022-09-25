class Solution:
    def isPalindrome(self, x: int) -> bool:
        copyX = x
        reversedX = 0
        while copyX > 0:
            reversedX *= 10
            reversedX += copyX % 10
            copyX = copyX // 10
        return x == reversedX


if __name__ == '__main__':
    solution = Solution()
    inputs = [
        121,  # True
        1221,  # True
        1223,  # False
    ]
    for input in inputs:
        print(solution.isPalindrome(input))