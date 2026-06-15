from typing import List

# There are 3 coloured balls, red, white, blue representing 0, 1, 2.
# The goal is simply to sort these balls in ascending order without using the inbuilt sort() or sorted()


class Solution:
    def bruteForceSortColors(self, nums):
        count0, count1, count2 = 0, 0, 0

        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1

        i = 0

        for _ in range(count0):
            nums[i] = 0
            i += 1
        for _ in range(count1):
            nums[i] = 1
            i += 1
        for _ in range(count2):
            nums[i] = 2
            i += 1
        return nums

    def optimalSortColors(self, nums:List[int]) -> List[int]:
        low, mid, high = 0, 0, len(nums) -1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

        return nums


if __name__ == "__main__":
    my_solution = Solution()
    nums = [2,0,2,1,1,0]

    print(my_solution.bruteForceSortColors(nums))

    print(my_solution.optimalSortColors(nums))