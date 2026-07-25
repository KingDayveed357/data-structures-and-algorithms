class Solution:
    """
    LeetCode 917: Reverse Only Letters

    This class provides a two-pointer approach to reverse only the alphabetic
    characters in a string while keeping all special characters and digits
    in their original positions.
    """

    def reverseOnlyLetters(self, s: str) -> str:
        # Step 1: Convert the immutable string into a mutable list to support character swaps.
        s = list(s)

        # Step 2: Initialize two pointers at opposite ends of the list.
        left = 0
        right = len(s) - 1

        # Step 3: Loop until the two pointers meet or cross in the middle.
        while left < right:

            # -------------------------------------------------------------------------
            # CHOOSE YOUR CHARACTER CHECKING METHOD (Choose Approach 1, 2, or 3)
            # -------------------------------------------------------------------------

            # APPROACH 1: Built-in Python String Method (Cleanest & Most Pythonic)
            # while left < right and not s[left].isalpha():
            #     left += 1
            # while left < right and not s[right].isalpha():
            #     right -= 1

            # APPROACH 2: Character Comparisons (Behind the scenes, Python uses ASCII)
            while left < right and not (('a' <= s[left] <= 'z') or ('A' <= s[left] <= 'Z')):
                left += 1
            while left < right and not (('a' <= s[right] <= 'z') or ('A' <= s[right] <= 'Z')):
                right -= 1

            # APPROACH 3: Explicit Numeric ASCII Code Checks using ord()
            # while left < right and not ((97 <= ord(s[left]) <= 122) or (65 <= ord(s[left]) <= 90)):
            #     left += 1
            # while left < right and not ((97 <= ord(s[right]) <= 122) or (65 <= ord(s[right]) <= 90)):
            #     right -= 1

            # -------------------------------------------------------------------------
            # WHY WE REPEAT 'left < right' IN THE INNER LOOPS:
            # If a string contains consecutive non-letters (e.g., "---abc"), an inner
            # loop could increment 'left' beyond 'right' or completely out of bounds.
            # Checking 'left < right' first ensures safe short-circuit evaluation.
            # -------------------------------------------------------------------------

            # Step 4: Swap the characters when both pointers land safely on valid letters.
            s[left], s[right] = s[right], s[left]

            # Step 5: Advance both pointers inward to look for the next pair of letters.
            left += 1
            right -= 1

        # Step 6: Convert the list back into a string and return it.
        return "".join(s)


if __name__ == "__main__":
    # Test execution block to verify functionality
    solution = Solution()
    test_string = "a9-bCdEf-ghIj"

    print("Original String: ", test_string)
    print("Reversed String: ", solution.reverseOnlyLetters(test_string))
