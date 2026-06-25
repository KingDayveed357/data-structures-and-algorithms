from typing import List

class Solution:
    def optimalTwoSum(self, numbers:List[int], target:int) -> List[int]:
         n = len(numbers)
         left, right = 0, n - 1

         while left < right:
             current_sum = numbers[left] + numbers[right]

             if current_sum == target:
                 return [left + 1, right + 1]

             elif current_sum < target:
                 left += 1

             else:
                 right -= 1

    def twoSumApproachTwo(self, numbers, target):
        def binarySearch(left, right, value):
            while left <= right:
                mid = (left + right) // 2

                if numbers[mid] == value:
                    return mid

                elif numbers[mid] > value:
                    right = mid - 1

                else:
                    left = mid + 1

            return -1

        for i in range(len(numbers)):
            complement = target - numbers[i]
            j = binarySearch(i + 1, len(numbers) - 1, complement)
            if j != -1:
                return [i+1, j+1]



if __name__ == "__main__":
    my_solution = Solution()
    numbers = [1, 2, 3, 4, 5, 6]
    target = 7
    # print(my_solution.optimalTwoSum(numbers,target))
    print(my_solution.twoSumApproachTwo(numbers, target))






