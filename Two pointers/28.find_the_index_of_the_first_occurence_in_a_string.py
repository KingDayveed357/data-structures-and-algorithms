class Solution:
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            found = True
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    found = False
                    break

            if found: return i

        return -1

"""Other string searching algorithms which can be used to optimize string searching are:
Algorithm	Idea	Time
Brute Force	Compare every position	O(n × m)
Rabin-Karp	Compare hashes instead of characters	Average O(n + m)
KMP (Knuth-Morris-Pratt) Never compare the same character twice	O(n + m)
Boyer-Moore	Compare from the end and jump far ahead	Often faster than O(n) in practice
Z Algorithm	Build a reusable match table	O(n + m)

"""




if __name__ == "__main__":
    my_solution = Solution()
    needle = "sad"
    haystack = "sadbutsad"
    print(my_solution.strStr(haystack, needle))