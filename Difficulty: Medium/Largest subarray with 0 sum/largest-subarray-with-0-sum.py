#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, a):
        preSumMap = {}
        Sum = 0
        maxLen = 0
        for i in range(n):
            Sum += a[i]
            if Sum == 0:
                maxLen = max(maxLen, i + 1)
            rem = Sum - 0
            if rem in preSumMap:
                length = i - preSumMap[rem]
                maxLen = max(maxLen, length)
            if Sum not in preSumMap:
                preSumMap[Sum] = i

        return maxLen


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends