// https://leetcode.com/problems/roman-to-integer/

/**
 * @param {string} s
 * @return {number}
 */
function romanToInt(s) {
  const letters = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
  const getDigit = c => c ? 10 ** (Math.floor(letters.indexOf(c) / 2)) : null
  const isBaseOne = c => letters.indexOf(c) % 2 === 0
  const maybeInitEntry = digit => { if (!(digit in intByDigit)) intByDigit[digit] = 0 }

  const intByDigit = {}
  let last = null

  s.split("").reverse().forEach(c => {
    const digit = getDigit(c)
    const lastDigit = getDigit(last)

    if (isBaseOne(c)) {
      if (!last) {
        intByDigit[digit] = 1
      } else if (lastDigit > digit || (lastDigit === digit && !isBaseOne(last))) {
        maybeInitEntry(digit)
        intByDigit[digit] -= 1
      } else {
        maybeInitEntry(digit)
        intByDigit[digit] += 1
      }
    } else {
      maybeInitEntry(digit)
      intByDigit[digit] += 5
    }

    last = c
  })

  let result = 0
  for (const [digit, value] of Object.entries(intByDigit))
    result += digit * value
  return result
};


const romanNumerals = [
  'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X',
  'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX',
  'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII', 'XXIX', 'XXX',
  'XXXI', 'XXXII', 'XXXIII', 'XXXIV', 'XXXV', 'XXXVI', 'XXXVII', 'XXXVIII', 'XXXIX', 'XL',
  'XLI', 'XLII', 'XLIII', 'XLIV', 'XLV', 'XLVI', 'XLVII', 'XLVIII', 'XLIX', 'L'
]

let convertedInts = ''
let results = []
for (const [i, numeral] of romanNumerals.entries()) {
  const convertedInt = romanToInt(numeral)
  convertedInts += String(convertedInt) + ', '
  results.push(convertedInt === i + 1)
}

console.log(convertedInts)
console.log(!results.includes(false) ? 'OK!' : 'ERROR')