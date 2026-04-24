
class Solution:
    def furthest_distance_from_origin(self, moves):
        balance = 0
        blanks = 0

        for m in moves:
            if (m == "L"):
                balance -= 1
            elif (m == "R"):
                balance += 1
            else:
                blanks += 1

        return abs(balance) + blanks


solution = Solution()
print(solution.furthest_distance_from_origin("L_R_L__R"))