from typing import List

class Solution:
    def applyOperations(self, nums:List[int]) -> List[int]:
        n = len(nums)

        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0


        k = 0

        for i in range(n):
            if nums[i] != 0:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1

        return nums


if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,2,1,1,0]
    print(solution.applyOperations(nums))