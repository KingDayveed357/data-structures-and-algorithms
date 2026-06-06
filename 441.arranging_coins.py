class Solution:
    def bruteForceArrangeCoins(self, n: int) -> int:
        row = 1

        while n >= 1:
            n -= row
            row += 1

        return row - 1

    def binarySearchArrangeCoins(self, n:int) -> int:
        left, right = 0, n
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            coins_used = mid * (mid + 1) // 2

            if coins_used <= n:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans

    def optimalArrangeCoins(self, n:int) -> int:



if __name__ == "__main__":
    my_solution = Solution()
    n = 5

    print(my_solution.bruteForceArrangeCoins(n))


