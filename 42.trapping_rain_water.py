from typing import List


class Solution:
    """
    LeetCode 42 - Trapping Rain Water

    Three progressively optimized solutions are provided:

    1. Brute Force
       - Time Complexity : O(n²)
       - Space Complexity: O(1)

    2. Prefix/Suffix Dynamic Programming
       - Time Complexity : O(n)
       - Space Complexity: O(n)

    3. Two Pointers (Optimal)
       - Time Complexity : O(n)
       - Space Complexity: O(1)
    """

    def bruteForceTrap(self, height: List[int]) -> int:
        """
        Brute Force Approach

        For every index:
            1. Find the tallest bar on its left.
            2. Find the tallest bar on its right.
            3. Water above this bar is

                    min(leftMax, rightMax) - currentHeight

        Since we recompute the left and right maximum for every index,
        many calculations are repeated, resulting in O(n²) time.
        """

        n = len(height)
        water = 0

        # Visit every bar in the elevation map.
        for i in range(n):

            # Tallest wall seen on the left and right of index i.
            leftMax = 0
            rightMax = 0

            # Scan from the beginning to the current index.
            for j in range(i + 1):
                leftMax = max(leftMax, height[j])

            # Scan from the current index to the end.
            for j in range(i, n):
                rightMax = max(rightMax, height[j])

            # Water level is determined by the shorter boundary.
            water += min(leftMax, rightMax) - height[i]

        return water

    def prefixSuffixTrap(self, height: List[int]) -> int:
        """
        Prefix/Suffix Dynamic Programming

        Observation:
        The brute force solution repeatedly computes the same left and
        right maximum values.

        Instead, precompute:

            left_max[i]
                = tallest wall from index 0 -> i

            right_max[i]
                = tallest wall from index i -> n-1

        Once both arrays are built, computing trapped water becomes
        a single linear pass.
        """

        n = len(height)

        if n == 0:
            return 0

        # left_max[i] stores the tallest wall seen from the left.
        left_max = [0] * n

        # right_max[i] stores the tallest wall seen from the right.
        right_max = [0] * n

        # First bar is its own left maximum.
        left_max[0] = height[0]

        # Build prefix maximum array.
        #
        # Example:
        # height   = [4,2,0,3,2,5]
        # left_max = [4,4,4,4,4,5]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        # Last bar is its own right maximum.
        right_max[n - 1] = height[n - 1]

        # Build suffix maximum array.
        #
        # Example:
        # height    = [4,2,0,3,2,5]
        # right_max = [5,5,5,5,5,5]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        water = 0

        # Compute trapped water at every position.
        for i in range(n):
            water += min(left_max[i], right_max[i]) - height[i]

        return water

    def optimalTrap(self, height: List[int]) -> int:
        """
        Two Pointer Approach (Optimal)

        Key Insight
        -----------
        The DP solution stores two arrays:

            left_max[]
            right_max[]

        We actually don't need the entire arrays.

        Instead, we maintain only:

            left_max
            right_max

        while moving two pointers inward.

        Why does this work?

        Whenever:

            height[left] < height[right]

        the left side becomes the limiting boundary.

        Therefore,

            min(left_max, right_max)

        is guaranteed to be left_max.

        So we can immediately compute the water above the left bar.

        Likewise, when the right wall is shorter,
        the right boundary becomes the limiting boundary.
        """

        n = len(height)

        if n == 0:
            return 0

        # Start pointers from both ends.
        left = 0
        right = n - 1

        # Tallest walls encountered so far.
        left_max = 0
        right_max = 0

        # Running total of trapped water.
        water = 0

        while left < right:

            # The shorter side determines the current water level.
            if height[left] < height[right]:

                # Found a new tallest wall on the left.
                if height[left] >= left_max:
                    left_max = height[left]

                else:
                    # Water trapped above the current left bar.
                    water += left_max - height[left]

                left += 1

            else:

                # Found a new tallest wall on the right.
                if height[right] >= right_max:
                    right_max = height[right]

                else:
                    # Water trapped above the current right bar.
                    water += right_max - height[right]

                right -= 1

        return water


if __name__ == "__main__":

    solution = Solution()

    height = [4, 2, 0, 3, 2, 5]

    print("Brute Force Approach :", solution.bruteForceTrap(height))
    print("Dynamic Programming  :", solution.prefixSuffixTrap(height))
    print("Two Pointer Approach :", solution.optimalTrap(height))