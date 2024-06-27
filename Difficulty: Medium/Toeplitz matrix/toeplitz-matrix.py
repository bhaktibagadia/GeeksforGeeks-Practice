# You are required to complete this method
# Return True/False or 1/0
def isToepliz(mat):
    #code here
    m, n = len(mat), len(mat[0])
    
    for i in range(1, m):
        for j in range(1, n):
            if mat[i][j]!=mat[i-1][j-1]:
                return False
    return True            


#{ 
 # Driver Code Starts
# Your code goes here
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(m)] for j in range(n)]
        k = 0
        for i in range(n):
            for j in range(m):
                matrix[i][j] = arr[k]
                k += 1
        b = isToepliz(matrix)

        if b == True:
            print("true")
        else:
            print("false")

# } Driver Code Ends