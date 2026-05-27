from typing import List
from collections import Counter

class Solution:
    def BruteForceSolution(self, nums:List[List[int]]) -> List:
        result = []

        for num in nums[0]:
            found_in_all = True

            for i in range(1, len(nums)):
                if num not in nums[i]:
                    found_in_all = False
                    break

            if found_in_all:
                result.append(num)

        return sorted(result)

    def OptimizedSolution(self, nums: List[List[int]]) -> List[int]:
        count = Counter()

        for arr in nums:
            for num in arr:
                count[num] += 1


        result = []
        n = len(nums)

        for num in count:
            if count[num] == n:
                result.append(num)

        return sorted(result)




if __name__ == "__main__":
    solution = Solution()
    nums = [[3,1,2,4,5],[3,2,3,4],[3,4,5,6]]

    # print("Brute Force Solution:", solution.BruteForceSolution(nums))
    print("Optimized Solution:", solution.OptimizedSolution(nums))


