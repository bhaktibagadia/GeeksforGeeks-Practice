class Solution:
    def rotateMatrix(self, k, mat):
        # code here
        x=k%len(mat[0])
        if x==0:
            return mat
        for i in range(len(mat)):
            mat[i]=mat[i][x:]+mat[i][:x]
        return mat    
                



#{ 
 # Driver Code Starts
import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().strip().split(" "))
        mat = []
        for i in range(n):
            mat.append(list(map(int, input().strip().split(" "))))
        ob = Solution()
        ans = ob.rotateMatrix(k, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end=" ")
            print()

# } Driver Code Ends