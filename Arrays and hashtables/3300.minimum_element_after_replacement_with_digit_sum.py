from typing import List

class Solution:
    def BruteForceSolution(self, nums):
        def digitSum(n):
            total = 0
            while n > 0:
                total  += n % 10
                n //= 10
            return total

        transformed = []

        for num in nums:
            transformed.append(digitSum(num))
        return min(transformed)


    def OptimizedSolution(self, nums:List[int]) -> int:
        def digitSum(n):
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total

        min_val = float("inf")

        for num in nums:
            min_val = min(min_val, digitSum(num))
        return min_val


if __name__ == "__main__":
    solution = Solution()

    nums = [10, 12, 13 ,14, 15]

    print("Brute Force:", solution.BruteForceSolution(nums))
    print("Optimized Solution:", solution.OptimizedSolution(nums))
