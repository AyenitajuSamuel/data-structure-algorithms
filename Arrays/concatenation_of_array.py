"""
Problem Description:
    Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

    Specifically, ans is the concatenation of two nums arrays.

    Return the array ans.

Constraints:
    n == nums.length
    1 <= n <= 1000
    1 <= nums[i] <= 1000

Approach: 
    To solve this problem, we can simply concatenate the input array with itself. This can be done using list concatenation in Python.

    Steps:
    1. Take the input array `nums`.
    2. Create a new array `ans` by concatenating `nums` with itself.
"""

class Solution:
    def getConcatenation(self, nums):
        ans = nums * 2
        return ans

solution = Solution()

#test
num_list = [1,3,2,1]
print(solution.getConcatenation(num_list))
