#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
		product, maxproduct = 1, -1e9
		for el in arr:
		    product*=el
		    maxproduct=max(maxproduct, product)
		    if product==0:
		        product=1
		        
		arr=arr[::-1]
		product=1
		for el in arr:
		    product*=el
		    maxproduct=max(maxproduct, product)
		    if product==0:
		        product=1
		
		return maxproduct       


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends