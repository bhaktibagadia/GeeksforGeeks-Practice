#User function template for Python

class Solution:
    def rectanglesInCircle(self,r):
        #code here
        rectangles=0
        diameter=2*r
        diametersquare=diameter*diameter
        for a in range(1, diameter):
            for b in range(1, diameter):
                diagonallength=(a*a + b*b)
                if diagonallength<=diametersquare:
                    rectangles+=1
        return rectangles            


#{ 
 # Driver Code Starts
#Initial Template for Python

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.rectanglesInCircle(N)
        print(ans)

# } Driver Code Ends