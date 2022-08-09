# https://leetcode.com/problems/roman-to-integer/

from collections import defaultdict


class Solution:
    def __init__(self):
        self.letters = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

    def romanToInt(self, s: str) -> int:
        intByDigit = defaultdict(int)
        last = None

        for c in reversed(s):
            digit = self._getDigit(c)
            lastDigit = self._getDigit(last)

            if self._isBaseOne(c):
                if not lastDigit:
                    intByDigit[digit] += 1
                elif lastDigit == digit and not self._isBaseOne(last):
                    intByDigit[digit] -= 1
                elif lastDigit > digit:
                    intByDigit[digit] -= 1
                else:
                    intByDigit[digit] += 1
            else:
                intByDigit[digit] += 5

            last = c

        result = sum(digit * value for digit, value in intByDigit.items())
        return result

    def _getDigit(self, c):
        return c and 10 ** (self.letters.index(c) // 2)

    def _isBaseOne(self, c):
        return self.letters.index(c) % 2 == 0


if __name__ == '__main__':
    solution = Solution()
    romanNumerals = [
        'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',
        'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX',
        'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII', 'XXIX', 'XXX',
        'XXXI', 'XXXII', 'XXXIII', 'XXXIV', 'XXXV', 'XXXVI', 'XXXVII', 'XXXVIII', 'XXXIX', 'XL',
        'XLI', 'XLII', 'XLIII', 'XLIV', 'XLV', 'XLVI', 'XLVII', 'XLVIII', 'XLIX', 'L'
    ]
    for numeral in romanNumerals:
        print(solution.romanToInt(numeral))
