from typing import List
from collections import defaultdict

class Solution:
    def bruteForceCountQuadruplets(self, nums: List[int]) -> int:
        count, n = 0, len(nums)

        for a in range(n):
            for b in range(a+1, n):
                for c in range(b+1, n):
                    for d in range(c+1, n):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            count += 1

        return count

    def optimizedCountQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        diff = defaultdict(int)

        for b in range(n - 3, 0, - 1):
            c = b + 1

            for d in range(c + 1, n):
                diff[nums[d] - nums[c]] += 1

            for a in range(b):
                ans += diff[nums[a] + nums[b]]
        return ans


if __name__ == "__main__":
    my_solution = Solution()
    nums = [1,1,1,3,5]
    print("Brute Force Approach:", my_solution.bruteForceCountQuadruplets(nums))
    print("Optimized Approach (Using HashMap):", my_solution.optimizedCountQuadruplets(nums))







