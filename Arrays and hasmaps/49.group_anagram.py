from typing import List
from collections import defaultdict


class Solution:
      def groupAnagrams(self, strs:List[str]) -> List[List[str]]:
            hashMap = defaultdict(list)
            for word in strs:
                  count = [0] * 26
                  for char in word:
                       count[ord(char) - ord('a')] += 1

                  hashMap[tuple(count)].append(word)
            return hashMap.values()


sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))