# https://leetcode.com/problems/roman-to-integer/

from collections import defaultdict


class Solution:
    def romanToInt(self, s: str) -> int:
        intByDigit = defaultdict(int)
        last = None

        for c in reversed(s):
            digit = self._getDigit(c)
            lastDigit = self._getDigit(last)

            if self._isBaseOne(c):
                if not last:
                    intByDigit[digit] += 1
                elif lastDigit > digit or (lastDigit == digit and not self._isBaseOne(last)):
                    intByDigit[digit] -= 1
                else:
                    intByDigit[digit] += 1
            else:
                intByDigit[digit] += 5

            last = c

        result = sum(digit * value for digit, value in intByDigit.items())
        return result

    def __init__(self):
        self.letters = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

    def _getDigit(self, c):
        return c and 10 ** (self.letters.index(c) // 2)

    def _isBaseOne(self, c):
        return self.letters.index(c) % 2 == 0


if __name__ == '__main__':
    romanNumerals = [
        'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',
        'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX',
        'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII', 'XXIX', 'XXX',
        'XXXI', 'XXXII', 'XXXIII', 'XXXIV', 'XXXV', 'XXXVI', 'XXXVII', 'XXXVIII', 'XXXIX', 'XL',
        'XLI', 'XLII', 'XLIII', 'XLIV', 'XLV', 'XLVI', 'XLVII', 'XLVIII', 'XLIX', 'L'
    ]

    solution = Solution()
    convertedInts = ''
    results = []
    for i, numeral in enumerate(romanNumerals):
        convertedInt = solution.romanToInt(numeral)
        convertedInts += str(convertedInt) + ', '
        results.append(convertedInt == i + 1)

    print(convertedInts[:-2])
    print('OK!' if False not in results else 'ERROR')
