# Promlems with the 2D matrix. How do I aasign vlaues from 2D matrix to list without going out of bounds!!!?!!?

import numpy as np
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # length of the matrix for number of rows
        m = len(matrix)
        # length of the matrix for number of cols
        n = len(matrix[0])
        # initializing the variables for counters
        i = 0
        r = 0
        c = 0
        dir = 1 # using direction as flag
        resultant = []*(m*n)
        print(m*n)
        while(i<m*n):
            print(matrix[r][c])
            x = matrix[r][c]
            resultant[i].append(x)
            print(resultant[i])
            # to move in the upward direction
            if dir==1:
                if c==n-1: # if reached the last column
                    r+=1
                    dir = -1
                elif r==0: # if at the first row
                    c+=1
                    dir = -1
                else: # normally loop increment the variables
                    r-=1
                    c+=1
            else:
                if r==m-1:
                    c+=1
                    dir = 1
                elif c==0:
                    r+=1
                    dir = 1
                else:
                    r+=1
                    c-=1
            i +=1
        return resultant

s = Solution()
matrix = [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
          ]
res = s.findDiagonalOrder(matrix)
print(res)
