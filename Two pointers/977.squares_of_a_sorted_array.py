from typing import List

class Solution:
    def sortedSquares(self, nums:List[int]) ->List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pos = n - 1

        while left <= right:
            left_sqr = nums[left] ** 2
            right_sqr = nums[right] ** 2

            if left_sqr > right_sqr:
                result[pos] = left_sqr
                left += 1

            else:
                result[pos] = right_sqr
                right -= 1

            pos -= 1

        return result

if __name__ == "__main__":
    solution = Solution()
    # nums = [-4,-1,0,3,10]
    nums = [11,-3,2,3,-7]
    print(solution.sortedSquares(nums))