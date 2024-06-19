from math import sqrt

class Solution:
    def maxVolume(self, P, A):
        l = (P - sqrt(P * P - 24 * A)) / 12
        h=P/4-2*l
        V = l * l*h
        return V




#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        perimeter, area = [int(x) for x in input().split()]

        ob = Solution()
        print('%.2f' % ob.maxVolume(perimeter, area))

# } Driver Code Ends