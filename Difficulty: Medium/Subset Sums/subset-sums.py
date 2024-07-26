#User function Template for python3
class Solution:
	def subsetSums(self, arr, n):
		# code here
		def rec(i, ds):
		    if i==len(arr):
		        ans.append(sum(ds))
		        return
		    ds.append(arr[i])
		    rec(i+1, ds)
		    ds.pop()
		    rec(i+1, ds)
		ans=[]
		rec(0, [])
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