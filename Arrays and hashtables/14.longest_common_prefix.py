class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        reference_word = strs[0]

        for i in range(len(reference_word)):
            char_to_match = reference_word[i]

            for word in strs[1:]:
                if i == len(word) or word[i] != char_to_match:
                   return reference_word[:i]
        return reference_word






sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))