
class Solution:
    def reverseStr(self, s:str, k:int):
        left , right = 0, k - 1

        while left < right:

            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s





if __name__ == "__main__":
    solution = Solution()
    s = "abcdefg"
    k = 2
    print(solution.reverseStr(s, k))