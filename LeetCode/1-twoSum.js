// https://leetcode.com/problems/two-sum/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
function twoSum(nums, target) {
  const complementByNum = {}
  for (const [i, num] of nums.entries()) {
    const complement = target - num
    if (complement in complementByNum)
      return [nums.indexOf(complement), i]
    complementByNum[num] = complement
  }
};


[
  [[2,7,11,15], 9],  // [0, 1]
  [[3,2,4], 6],  // [1,2]
  [[3,3], 6],  // [0,1]
  [[-3,4,3,90], 0],  // [0, 2]
].forEach(input => console.log(twoSum(...input)))
