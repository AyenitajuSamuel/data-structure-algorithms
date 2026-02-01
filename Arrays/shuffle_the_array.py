"""
Problem Description:
    Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
    Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Constraints:
    1 <= n <= 500
    nums.length == 2n
    1 <= nums[i] <= 10^3

Approach:
    Split the array into two halves, then place elements from each half into a new array in an alternating fashion.

"""
class Solution:
    def shuffle(self, nums, n):
        first_side = nums[:n]
        second_side = nums[n:]
        final_list = []

        for i in range(len(first_side)):
            final_list.append(first_side[i])
            final_list.append(second_side[i])

        return final_list

#test case
solution = Solution()

num_list = [2,5,1,3,4,7]
print(solution.shuffle(num_list, 3))