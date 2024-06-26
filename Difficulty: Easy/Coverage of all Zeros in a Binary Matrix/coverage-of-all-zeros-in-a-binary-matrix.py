#User function Template for python3

class Solution:
	def findCoverage(self, matrix):
		# Code here
		def totalcoverage(x,y):
		    cov=0
		    if 0<=x+1<len(matrix) and matrix[x+1][y]==1:
		        cov+=1
		    if 0<=x-1<len(matrix) and matrix[x-1][y]==1:
		        cov+=1
		    if 0<=y+1<len(matrix[0]) and matrix[x][y+1]==1:
		        cov+=1
		    if 0<=y-1<len(matrix[0]) and matrix[x][y-1]==1:
		        cov+=1      
		    return cov
		    
		ans=0    
		for i in range(len(matrix)):
		    for j in range(len(matrix[0])):
		        if matrix[i][j]==0:
		            ans+=totalcoverage(i,j)
		return ans            
		        
		        
		        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ans = ob.findCoverage(matrix)
        print(ans)

# } Driver Code Ends