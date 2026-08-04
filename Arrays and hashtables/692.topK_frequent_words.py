from collections import Counter
from typing import List

class Solution:
    def bruteforceTopKFrequentWords(self, words, k):
        count = Counter(words)

        top_words = [key for key,word in count.most_common(k)]

        return top_words

    def optimalSolutionTopKFrequentWords(self, words:List[str], k:int) -> List[str]:
        counts = Counter(words)

        buckets = [[] for _ in range(len(counts) + 1)]

        for word,freq in counts.items():
            buckets[freq].append(word)

        result = []

        for i  in range(len(buckets) - 1, 0 , -1):
            if buckets[i]:
                buckets[i].sort()

            for word in buckets[i]:
                result.append(word)
                if len(result) == k:
                    return result






if __name__ == "__main__":
    solution = Solution()

    words = ["love","i","leetcode","i","love","coding"]
    k = 2

    print("Brute Force Attempt:", solution.bruteforceTopKFrequentWords(words, k) )
    print("Optimal Solution:", solution.optimalSolutionTopKFrequentWords(words,k))