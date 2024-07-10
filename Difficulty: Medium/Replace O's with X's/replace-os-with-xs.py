#User function Template for python3
class Solution:
    def fill(self, n, m, mat):
        # code here
        vis=[[0]*m for _ in range(n)]
        delta=[(1, 0), (0, 1), (0, -1), (-1, 0)]
        
        def dfs(row, col):
            vis[row][col]=1
            for delr, delc in delta:
                delrow, delcol = row+delr, col+delc
                if 0<=delrow<n and 0<=delcol<m:
                    if not vis[delrow][delcol] and mat[delrow][delcol]=='O':
                        dfs(delrow, delcol)
        
        for i in range(m):
            if mat[0][i]=='O':
                dfs(0, i)
        for i in range(m):
            if mat[n-1][i]=='O':
                dfs(n-1, i)
        for j in range(n):
            if mat[j][0]=='O':
                dfs(j, 0)
        for j in range(n):
            if mat[j][m-1]=='O':
                dfs(j, m-1)
                
        for i in range(n):
            for j in range(m):
                if not vis[i][j] and mat[i][j]=='O':
                    mat[i][j]='X'
        return mat            
                    
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str,input().split()))
            mat.append(s)
        
        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends