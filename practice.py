
# Return 3 numbers in the nums list that adds up to zero.
# NOTE: The index of these 3 numbers must not be equal
# The solution set must not contain all duplicate triplets

class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return result










my_solution = Solution()
nums = [-1,0,1,2,-1,-4]
print(my_solution.threeSum(nums))