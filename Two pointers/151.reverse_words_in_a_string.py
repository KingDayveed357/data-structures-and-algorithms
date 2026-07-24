""" Given: A string of words.
A word is defined by sequence of "NON SPACE CHARACTERS".
The words in s will be separated by at least one space

 Required: Return a string of the words in reversed order concatenated by a single space
 NOTE:  s may contain leading or trailing spaces or multiple spaces between two words.
 The returned string should only have a single space separating the words. Do not include any extra spaces.
"""
class Solution:
    def reverseWords(self, s:str) -> str:
        words = s.split()

        left = 0
        right = len(words) - 1

        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        # OR SIMPLY AND CLEANLY USING THE reverse() method
        # words.reverse()

        return " ".join(words)

# How do I join a string of characters in a List of strings to become a word?
# A word is a sequence of non space characters. Each word should be concatenated by a single space


if __name__ == "__main__":
    my_solution = Solution()
    s = "Jesus is Love"

    print(my_solution.reverseWords(s))