from typing import List
from collections import Counter
class Solution:
    def isPossibleToSplit(self, nums:List[int]):
        count = Counter(nums)

        for freq in count.values():
            if freq > 2:
                return False

        return True


if __name__ == "__main__":
    solution = Solution()

    # nums = [1, 1, 1, 1]
    nums = [1, 1, 2, 2, 3, 4]

    print("Solution:", solution.isPossibleToSplit(nums))