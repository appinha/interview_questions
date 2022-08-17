# https://leetcode.com/problems/longest-common-prefix/

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        i = 0
        while True:
            try: char1 = strs[0][i]
            except: return prefix

            for str in strs[1:]:
                try: char2 = str[i]
                except: return prefix

                if char1 != char2:
                    return prefix

            prefix += char1
            i += 1


if __name__ == '__main__':
    solution = Solution()
    inputs = [
        ["flower","flow","flight"],  # "fl"
        ["dog","racecar","car"],  # ""
        ["","racecar","car"],  # ""
        ["c","rr","rrr"],  # ""
    ]
    for input in inputs:
        print('"' + solution.longestCommonPrefix(input) + '"')
