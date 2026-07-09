from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Find the median of two sorted arrays using binary search.

        The key insight is to partition both arrays such that:
        - Left partition contains the first half of the combined elements
        - Right partition contains the second half
        - All elements in left partition ≤ all elements in right partition

        Time Complexity: O(log(min(m,n)))
        Space Complexity: O(1)
        """

        # OPTIMIZATION: Always perform binary search on the smaller array
        # This ensures we do minimal work - binary search on the smaller array
        # reduces the time complexity from O(log(m+n)) to O(log(min(m,n)))
        # Note: We swap so nums1 is always the smaller array for binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # Get lengths of both arrays after potential swap
        # m is the smaller array length, n is the larger array length
        m, n = len(nums1), len(nums2)

        # Calculate the total number of elements and the halfway point
        # half represents how many elements should be in the left partition
        # For even total: left and right partitions will have equal elements
        # For odd total: left partition will have one more element
        total = m + n
        half = total // 2

        # Binary search boundaries for partition point in the smaller array (nums1)
        # left: minimum possible elements from nums1 in left partition
        # right: maximum possible elements from nums1 in left partition
        left, right = 0, m

        # Binary search to find the correct partition point
        while left <= right:
            # i: number of elements from nums1 in the left partition
            # This is our binary search mid-point for nums1
            i = (left + right) // 2

            # j: number of elements from nums2 in the left partition
            # Since half elements should be in left partition total,
            # and i elements come from nums1, the rest must come from nums2
            j = half - i

            # Define the four boundary elements around the partition
            # Aleft: largest element in left partition from nums1
            # If no elements from nums1 in left partition (i=0), use -infinity
            Aleft = nums1[i - 1] if i > 0 else float("-inf")

            # Aright: smallest element in right partition from nums1
            # If all elements from nums1 in left partition (i=m), use +infinity
            Aright = nums1[i] if i < m else float("inf")

            # Bleft: largest element in left partition from nums2
            # If no elements from nums2 in left partition (j=0), use -infinity
            Bleft = nums2[j - 1] if j > 0 else float("-inf")

            # Bright: smallest element in right partition from nums2
            # If all elements from nums2 in left partition (j=n), use +infinity
            Bright = nums2[j] if j < n else float("inf")

            # CHECK: Is this partition correct?
            # Condition: max left ≤ min right for both arrays
            # Note: The check Bleft <= Bright is always true since arrays are sorted,
            # so we only need to check cross-boundary conditions
            if Aleft <= Bright and Bleft <= Aright:
                # FOUND THE CORRECT PARTITION!

                # If total length is odd: median is the minimum of right partition
                # Because left partition has one more element in odd case
                if total % 2:
                    return min(Aright, Bright)

                # If total length is even: median is average of:
                # - max of left partition (largest element on left side)
                # - min of right partition (smallest element on right side)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            # PARTITION IS INCORRECT - ADJUST BINARY SEARCH:

            # Case 1: Left partition of nums1 is too large
            # Aleft > Bright means we have too many elements from nums1 in left partition
            # We need to reduce i - move right boundary left
            elif Aleft > Bright:
                right = i - 1

            # Case 2: Left partition of nums1 is too small
            # Bleft > Aright means we have too few elements from nums1 in left partition
            # We need to increase i - move left boundary right
            else:
                left = i + 1


if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Odd total length
    # nums1 = [1, 3], nums2 = [2]
    # Expected output: 2.0 (merged: [1, 2, 3])
    # nums1 = [1, 3]
    # nums2 = [2]

    # Test case 2: Even total length
    # nums1 = [1, 2], nums2 = [3, 4]
    # Expected output: 2.5 (merged: [1, 2, 3, 4])
    nums1 = [1, 2]
    nums2 = [3, 4]

    # Print the computed median
    print(solution.findMedianSortedArrays(nums1, nums2))