from typing import List
from itertools import permutations
class Solution:
    def bruteForceAsteroidDestroyed(self, mass:int, asteroids:List[int]) -> bool:
        for order in permutations(asteroids):
            current_mass = mass

            for asteroid in order:
                if current_mass < asteroid:
                   break
                current_mass += asteroid
            return True
        return False


if __name__ == "__main__":
    solution = Solution()
    mass = 10
    asteroids = [ 3,9,19,5,21]
    print("Brute Force Solution:", solution.bruteForceAsteroidDestroyed(mass, asteroids))