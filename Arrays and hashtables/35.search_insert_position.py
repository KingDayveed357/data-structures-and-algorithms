### Binary Search Algorithm
# Works by using two pointers (left and right) to set boundaries in the List

from typing import List

class Solution:
    def searchIndex(self, nums:List[int], target:int) -> int:
        """
                Problem:
                Given a sorted array of distinct integers, return the index of the target
                if found. If not, return the index where it should be inserted.

                Approach:
                Use Binary Search to efficiently narrow down the search space.
                - If target is found → return its index
                - If not found → return the insertion position

                Key Insight:
                At the end of the binary search, 'left' will point to the correct
                insertion index (the first position where target can fit).

                Time Complexity: O(log n)
                Space Complexity: O(1)
                """

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left+right) // 2

            if (nums[mid] == target):
                return mid

            if (nums[mid] < target):
                left = mid + 1

            else:
                right = mid - 1

        return left



solution = Solution()
print(solution.searchIndex([1, 3, 5, 6], 7))

