# https://leetcode.com/problems/ransom-note/

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteCounter = Counter(ransomNote)
        magazineCounter = Counter(magazine)

        if not set(ransomNoteCounter).issubset(magazineCounter):
            return False

        magazineCounter.subtract(ransomNoteCounter)
        for value in magazineCounter.values():
            if value < 0:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    inputs = [
        ['a', 'b'],
        ['aa', 'ab'],
        ['aa', 'aab'],
    ]
    for input in inputs:
        print(solution.canConstruct(*input))
