from typing import List

class Solution:

    # 1. Brute Force — O(n^3)
    def threeSum_bruteforce(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        res.add(triplet)

        return [list(t) for t in res]


    #  2. Better (Hashing) — O(n^2)
    def threeSum_hashing(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()

        for i in range(n):
            seen = set()
            target = -nums[i]

            for j in range(i+1, n):
                complement = target - nums[j]

                if complement in seen:
                    triplet = tuple(sorted([nums[i], nums[j], complement]))
                    res.add(triplet)

                seen.add(nums[j])

        return [list(t) for t in res]


    #  3. Optimal (Two Pointers) — O(n^2)
    def threeSum_optimal(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            # skip duplicate anchor
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    # skip duplicates
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1

        return res


#  Test Runner
if __name__ == "__main__":
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]

    print("Brute Force:", solution.threeSum_bruteforce(nums))
    print("Hashing:", solution.threeSum_hashing(nums))
    print("Optimal:", solution.threeSum_optimal(nums))