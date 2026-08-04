from typing import List

class Solution:
    def brute_force_plus_one(self, digits):
        join_numbers =  int("".join(map(str, digits))) + 1
        return join_numbers

    def optimized_plus_one(self, digits:List[int]) -> int:
        n = len(digits)

        for i in range(n - 1, -1 , -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits

solution = Solution()
print(solution.brute_force_plus_one([9]))
print(solution.optimized_plus_one([9,9,9]))