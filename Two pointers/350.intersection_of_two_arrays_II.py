from typing import List
from collections import Counter

class Solution:
    def BruteForceSolution(self, nums1:List[int], nums2:List[int]) -> List[int]:
        result = []

        for num in nums1:
          if num in nums2:
              result.append(num)
              nums2.remove(num)

        return result

    def TwoPointerSolution(self, nums1:List[int], nums2:List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        result = []
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
               result.append(nums1[i])
               i += 1
               j += 1

            elif nums1[i] < nums2[j]:
                i += 1

            else:
                j += 1
        return result



    def OptimizedSolution(self, nums1:List[int], nums2:List[int]) -> List[int]:
        count = Counter(nums1)
        result = []

        for num in nums2:
            if count[num] > 0:
                result.append(num)
                count[num] -= 1

        return result






if __name__ == "__main__":
    solution = Solution()
    # nums1 = [4,9,5]
    # nums2 = [9,4,9,8,4]

    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]


    # print("Brute Force:", solution.BruteForceSolution(nums1, nums2))
    # print("Two Pointer Solution:", solution.TwoPointerSolution(nums1, nums2))
    print("Optimized Solution:", solution.OptimizedSolution(nums1, nums2))