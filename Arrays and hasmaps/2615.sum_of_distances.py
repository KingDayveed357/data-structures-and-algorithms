from collections import defaultdict

class Solution:
    def bruteForceDistance(self, nums):
        n = len(nums)
        arr = [0] * n

        for i in range(n):
            for j in range(n):
                if i != j and nums[i] == nums[j]:
                    arr[i] += abs(i-j)
        return arr

    def optimizedDistance(self, nums):
        arr = [0] * len(nums)
        groups = defaultdict(list)

        for i, num in enumerate(nums):
            groups[num].append(i)

        for indices in groups.values():
            prefix_sum = [0]

            for idx in indices:
                prefix_sum.append(prefix_sum[-1] + idx)

            k = len(indices)

            for i in range(k):
                index = indices[i]

                left = index * i - prefix_sum[i]

                right = (prefix_sum[k] - prefix_sum[i+1]) - index * (k - i - 1)
                arr[index] = left + right
        return arr




if __name__ == "__main__":


    my_solution = Solution()
    nums = [1,3,1,1,2]
    print(my_solution.bruteForceDistance(nums))
    print(my_solution.optimizedDistance(nums))