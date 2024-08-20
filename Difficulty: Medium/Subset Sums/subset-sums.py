#User function Template for python3
class Solution:
	def subsetSums(self, arr, n):
		# code here
		ans = []
		def rec(l, r, cursum):
		    if l>r:
		        ans.append(cursum)
		        return
		    rec(l+1, r, cursum+arr[l])
		    rec(l+1, r, cursum)
		rec(0, n-1, 0)
		ans.sort()
		return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x, end=" ")
        print("")

# } Driver Code Ends