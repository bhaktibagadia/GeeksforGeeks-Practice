#User function Template for python3

class Solution:
    
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr, n):
        ##Your code here
        maxsum, summ = -1e9, 0
        for num in arr:
            summ+=num
            maxsum=max(maxsum, summ)
            if summ<0:
                summ=0
        return maxsum        





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        n = int(input())

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr, n))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends