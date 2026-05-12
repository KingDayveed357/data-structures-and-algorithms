
class Solution:
    def twoSum_bruteforce(self, nums: list[int], target: int) -> list[int]:

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j

        return []


    def twoSum_optimal(self, nums: list[int], target: int) -> int:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return (seen[complement], i)

            seen[num] = i

        return []

# Test Runner
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9

    print("Brute Force:", solution.twoSum_bruteforce(nums, target))
    print("Optimal Solution:", solution.twoSum_optimal(nums, target))