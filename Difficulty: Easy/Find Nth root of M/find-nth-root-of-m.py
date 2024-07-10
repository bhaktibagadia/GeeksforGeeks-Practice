#User function Template for python3

class Solution:
	def NthRoot(self, n, m):
		# Code here
		if m==0:
		    return 0
		low, high = 1, m
		while low<=high:
		    mid=(low+high)//2
		    if mid**n==m:
		        return mid
		    elif mid**n>m:
		        high=mid-1
		    else:
		        low=mid+1
		return -1        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		ob = Solution()
		ans = ob.NthRoot(n, m)
		print(ans)
# } Driver Code Ends