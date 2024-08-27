#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        cursum = sum(Arr[:K])
        maxSum = cursum
        for i in range(N-K):
            cursum-=Arr[i]
            cursum+=Arr[i+K]
            maxSum = max(maxSum, cursum)
        return maxSum    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends