## Conditions:
# arr1 contains uniqueCnt1 distinct positive integers which is not divisble by divisor1
# arr2 contains uniqueCnt2 distinct positive integers which is not divisble by divisor2
# No integer is present in both arr1 and arr2

### Return Type: Maximum value present in either array

from typing import List
from math import gcd

class Solution:
    def minimizeSet(self, divisor1, divisor2, uniqueCnt1, uniqueCnt2):
        def can(x):
            lcm = (divisor1 * divisor2) // gcd(divisor1, divisor2)

            count1 = x - (x // divisor1)
            count2 = x - (x // divisor2)
            common = x - (x // lcm)

            return (count1 >=uniqueCnt1 and
                    count2 >=uniqueCnt2 and
                    common >=uniqueCnt1 + uniqueCnt2)

        x = 1
        while True:
            if can(x):
                return x
            x += 1




if __name__ == "__main__":
    solution = Solution()
    divisor1,divisor2,uniqueCnt1,uniqueCnt2 = 2, 7, 1, 3

    print("Solution:", solution.minimizeSet(divisor1,divisor2,uniqueCnt1,uniqueCnt2))