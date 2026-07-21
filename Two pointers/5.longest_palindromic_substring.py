class LongestPalindromeSolution:
    def BruteForce(self, s:str) -> str:
        longest = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i : j+1]

                if substring == substring[::-1]:
                    if len(substring) > len(longest):
                        longest = substring

        return longest

   # Uses Two pointers following the Expand Around Center
    def Optimal(self, s):
        result = ""

        for i in range(len(s)):
            #for odd length
            left = right = i

            while left >=0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(result):
                    result = s[left : right+1]

                left -= 1
                right += 1

            left, right = i, i + 1

            while left >=0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(result):
                    result = s[left : right + 1]

                left -= 1
                right += 1

        return result


if __name__ == "__main__":
    my_solution = LongestPalindromeSolution()
    palindromic_string = "racecar"
    another_palindromic_string = "babababay"
    reg_string = "Aboy hwfa na"

    # print(my_solution.BruteForce(another_palindromic_string))
    print(my_solution.Optimal(another_palindromic_string))
