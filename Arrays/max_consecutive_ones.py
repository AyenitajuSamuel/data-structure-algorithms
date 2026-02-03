"""
Problem Description:
    Given a binary array nums, return the maximum number of consecutive 1's in the array.

    Example 1:
    Input: nums = [1,1,0,1,1,1]
    Output: 3
    Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Constraints:
    -1 <= nums.length <= 105
    -nums[i] is either 0 or 1.

Approach: 
    1. Initialize an empty list to store counts of consecutive 1's and a counter set to zero.
    2. Iterate through each element in the input array:
        a. If the element is 1, increment the counter.
        b. If the element is 0, append the current count to the list and reset the counter to zero.
    3. After the loop, append the last count to the list (to account for trailing 1's).
    4. Return the maximum value from the list of counts.

"""
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count_list = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count_list.append(count)
                count = 0
        count_list.append(count)
        return max(count_list)

#test
solution = Solution()
num_list = [1, 1, 1, 1, 1, 0]
print(solution.findMaxConsecutiveOnes(num_list))