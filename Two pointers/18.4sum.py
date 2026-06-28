from typing import List

class Solution:
    def fourSum(self, nums:List[int], target) -> List[List[int]] :
        nums.sort()

        result = []
        n = len(nums)

        for i in range(n - 3):
            if i > 0  and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    current_sum = (nums[i] + nums[j] + nums[left] + nums[right])

                    if current_sum < target:
                        left += 1

                    elif current_sum > target:
                        right -= 1

                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
        return result


if __name__ == "__main__":
    my_solution = Solution()
    nums = [1, 2, 3, 4, 5]
    target = 10
    print(my_solution.fourSum(nums, target))





