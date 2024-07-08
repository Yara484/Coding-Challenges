class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix) # 3 
        cols = len(matrix[0]) # 4 
        numElements = rows * cols # 12
        l,r = 0, numElements - 1
        while l <= r:
            midpoint = (l+r) // 2 # 5 which is value 11 -> [1][1]
            # Getting indexes, using rows and cols
            rowIndex = midpoint // cols
            colIndex = midpoint % cols 
            element = matrix[rowIndex][colIndex]
            if element == target:
                return True
            elif element > target:
                r = midpoint - 1
            else:
                l = midpoint + 1
        return False                