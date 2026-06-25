from typing import List

### Brute Force Solution
# Time Complexity O(n)
# Space Complexity O(n)

class BruteForceSolution:
    def removeElement(self, nums:List[int], value:int) -> int:
        sorted_array = []

        for num in nums:
            if value != num:
                sorted_array.append(num)

        for i in range(len(sorted_array)):
            nums[i] = sorted_array[i]
        return len(sorted_array)


brute_force_solution = BruteForceSolution()
print(brute_force_solution.removeElement([3,2,2,3], 3))

### Optimized Solution
# Time Complexity: 0(n)
# Space Complexity: O(1)

class OptimizedSolution:
    def removeElement(self, nums:List[int], value:int) -> int:
        if not nums:
            return 0

        k = 0 # position to place the next valid number

        for i in range(len(nums)):
            if nums[i] != value:
                nums[k] = nums[i]
                k += 1
        return k





optimized_solution = OptimizedSolution()
print(optimized_solution.removeElement([3,2,2,3], 3))


