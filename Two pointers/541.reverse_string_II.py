
class Solution:
    def reverseStr(self, s:str, k:int):
        s = list(s)

        for start in range(0, len(s), 2*k):
            left = start
            right = min(start + k - 1, len(s) - 1)

            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return "".join(s)




if __name__ == "__main__":
    solution = Solution()
    s = "abcdefg"
    k = 2
    print(solution.reverseStr(s, k))