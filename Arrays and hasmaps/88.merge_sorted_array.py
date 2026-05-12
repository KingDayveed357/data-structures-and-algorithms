class BruteForceSolution:
    def merge(self, nums1, m, nums2, n):
        i = j = 0
        result = []

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        # Remaining
        while i < m:
            result.append(nums1[i])
            i += 1

        while j < n:
            result.append(nums2[j])
            j += 1

        # Copy back
        for i in range(len(result)):
            nums1[i] = result[i]





solution = BruteForceSolution()
print(solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3))

class OptimalSolution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1

            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        return nums1

optimizedSolution = OptimalSolution()
print(optimizedSolution.merge([1,2,3,0,0,0], 3, [2,5,6], 3))


