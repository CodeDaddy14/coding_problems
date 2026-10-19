class Solution:
    def spiralOrder(self, matrix):
        top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        left = 0
        res = []

        while top <= bottom and left <= right:

            # printiing top line
            for column in range(left, right+1):
                res.append(matrix[top][column])
            top +=1

            #printiing top to bottom
            for row in range(top, bottom +1):
                res.append(matrix[row][right])
            right-=1

            if top <= bottom:
                #bottom to left
                for column in range(right, left - 1, -1):
                    res.append(matrix[bottom][column])
                bottom-=1

            # from bottom left to up
            if left<=right:
                for row in range(bottom, top -1 ,-1):
                    res.append(matrix[row][left])
                left+=1
        
        return res
