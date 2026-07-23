from typing import List

class Solution:
    def flipAndInvertImage(self, image:List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            left = 0
            right = (len(image[i])) - 1
            while left <= right:
                if left == right:
                    image[i][left] = image[i][left] ^ 1
                else:
                    image[i][left], image[i][right] = image[i][right] ^ 1, image[i][left] ^ 1

                left += 1
                right -= 1

        return image


if __name__ == "__main__":
    solution = Solution()
    image = [[1,1,0],[0,0,1],[0,0,0]]
    # image = [[1,1,0],[0,0,1],[0,0,0]]
    print(solution.flipAndInvertImage(image))
