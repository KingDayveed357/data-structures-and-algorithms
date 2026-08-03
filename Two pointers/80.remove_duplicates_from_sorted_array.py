from typing import List
from collections import Counter

class Solution:
    def removeDuplicates(self, nums:List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        write = 2

        for read in range(2, len(nums)):
            if nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1

        return write


if __name__ == "__main__":
    solution = Solution()
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(solution.removeDuplicates(nums))