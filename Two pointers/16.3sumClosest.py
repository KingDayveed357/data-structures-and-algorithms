

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum

                if current_sum == target:
                    return current_sum

                elif current_sum < target:
                    left += 1

                else:
                    right -= 1

        return closest


my_solution = Solution()
nums, target = [-1,2,1,-4],  1
print(my_solution.threeSumClosest(nums, target))