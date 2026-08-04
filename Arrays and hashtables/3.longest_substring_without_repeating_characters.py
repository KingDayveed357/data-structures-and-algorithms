class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        char_map = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            current_char = s[right]

            if current_char in char_map and char_map[current_char] >= left:
                left = char_map[current_char] + 1

            char_map[current_char] = right
            current_window_size = right - left + 1
            max_length = max(max_length, current_window_size)

        return max_length


if __name__ == "__main__":
    solution = Solution()
    s = "Jesus"
    print(solution.lengthOfLongestSubstring(s))






