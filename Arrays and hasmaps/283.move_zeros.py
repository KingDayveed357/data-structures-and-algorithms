class Solution:
    def moveZeros(self, nums):
        k = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1

        return nums


my_solution = Solution()
nums = [0,1,0,3,12]
print(my_solution.moveZeros(nums))