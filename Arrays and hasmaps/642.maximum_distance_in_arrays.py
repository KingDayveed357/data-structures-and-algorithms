from typing import List

class Solution:

    def BruteForceSolution(self, arrays):

        max_dist = 0

        for i in range(len(arrays)):
            for j in range(len(arrays)):
                if i == j:
                    continue

                for a in arrays[i]:
                    for b in arrays[j]:
                        max_dist = max(max_dist, abs(a-b))

        return max_dist



    def OptimizedSolution(self, arrays:List[List[int]]) -> int:
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        result = 0

        for i in range(1, len(arrays)):
            current_min = arrays[i][0]
            current_max = arrays[i][-1]

            result = max(
                result,
                abs(current_max - min_val),
                abs(max_val - current_min)
            )

            min_val = min(min_val, current_min)
            max_val = max(max_val, current_max)

        return result

if __name__ == "__main__":
    solution = Solution()
    arrays = [[1,2,3],[4,5],[1,2,3]]

    print("Brute Force Solution:", solution.BruteForceSolution(arrays))
    print("Optimized Solution:", solution.OptimizedSolution(arrays))


