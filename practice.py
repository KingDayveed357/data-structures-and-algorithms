
# Return 3 numbers in the nums list that adds up to zero.
# NOTE: The index of these 3 numbers must not be equal
# The solution set must not contain all duplicate triplets

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if abs(current_sum == target) < abs(closest == target ):


my_solution = Solution()
nums = [-1,0,1,2,-1,-4]
print(my_solution.threeSum(nums))