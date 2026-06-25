from typing import List

"""
LeetCode 349: Intersection of Two Arrays

PROBLEM DEFINITION:
Given two integer arrays, return a unique array of their intersection.
Each element in the result must be unique and can appear in any order.

ENGINEERING STRATEGIES:

1. BRUTE FORCE APPROACH:
   - Logic: Iterate through nums1, and for each element, scan nums2 for a match.
   - Uniqueness: Check if the match already exists in the result list before adding.
   - Time Complexity: O(N * M) - Inefficient for larger datasets.
   - Space Complexity: O(min(N, M)) - For the output storage.

2. OPTIMIZED APPROACH (Hash Sets):
   - Logic: Convert the first array into a Hash Set for O(1) average lookup time.
     Filter the second array against this set.
   - Uniqueness: Use a second set (or a set-based intersection) to naturally
     handle duplicate entries in nums2.
   - Time Complexity: O(N + M) - Linear time execution.
   - Space Complexity: O(N) - To store the lookup set.

3. TWO-POINTER APPROACH (Memory Constrained):
   - Logic: Sort both arrays. Use two pointers (i, j) to traverse both arrays 
     simultaneously. Move pointers based on value comparison.
   - Uniqueness: Only add to result if the current match is different from the 
     last added element.
   - Time Complexity: O(N log N + M log M) - Dominated by sorting.
   - Space Complexity: O(1) - (Excluding output array) ideal for embedded logic.
"""

## BRUTE FORCE SOLUTION (Beginner Friendly approach, not efficient)
class BruteForceSolution:
    def intersection(self, nums1, nums2):
        result = []

        for num1 in nums1:
            for num2 in nums2:
              if num1 == num2:
                  if num1 not in result:
                     result.append(num1)
                  break

        return result


my_brute_force_solution = BruteForceSolution()
# print(my_brute_force_solution.intersection([1,2,2,1], [2,2]
# ))



## OPTIMIZED SOLUTION (Most efficient solution)
# class OptimizedSolution:
#     def intersection(self, nums1:List[int], nums2:List[int]) -> List[int]:
        



# my_optimized_solution = OptimizedSolution()
# print(my_optimized_solution.intersection([4,9,5],[9,4,9,8,4]
# ))


## TWO POINTERS APPROACH
class TwoPointersSolution:
    def intersection(self, nums1:List[int], nums2:List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        result:List[int] = []
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if not result or result[-1] != result:
                    result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1

            else:
                j += 1

        return result

two_pointers = TwoPointersSolution()
print(two_pointers.intersection([4,9,5],[9,4,9,8,4]
))