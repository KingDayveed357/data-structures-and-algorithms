from typing import List

nums_array  = [1,1,2]

### Brute Force Solution
class BruteForceSolution():
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        unique = [];

        for num in nums:
            if num not in unique:
                unique.append(num)

        for i in range(len(unique)):
            nums[i] = unique[i]

        return len(unique)

brute_force_solution = BruteForceSolution()
print(brute_force_solution.removeDuplicates(nums_array))

# Optimized Solution using Two pointers approach
### params:
# - i is the last unique element
# - j is the scanning pointer

### Time Complexity is of O(n)
### Space Complexity is of O(n)


class OptimizedSolution:
    def removeDuplicates(self, nums:List[int]) -> int:
        if not nums:
            return 0

        i = 0

        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1


optimized_solution = OptimizedSolution()
print(optimized_solution.removeDuplicates(nums_array))