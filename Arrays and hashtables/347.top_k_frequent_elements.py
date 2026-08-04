from typing import List
from collections import Counter

class Solution:
    def bruteForceTopKFrequent(self, nums, k):
        counts = Counter(nums)

        top_keys = [ key for key, count in counts.most_common(k)]

        return top_keys


    def optimalSolutionTopKFrequent(self, nums:List[int], k:int) -> List[int]:
        count = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for num,freq in count.items():
            buckets[freq].append(num)

        res = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)

                if len(res) == k:
                   return res

if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2
    solution = Solution()
    print("My Brute Force Solution:", solution.bruteForceTopKFrequent(nums, k))
    print("Optimized Solution:", solution.optimalSolutionTopKFrequent(nums, k))

