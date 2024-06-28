#User function Template for python3

class Solution:
    def pattern (self, arr):
        # code here
        for i in range(len(arr)):
            if arr[i]==arr[i][::-1]:
                return str(i)+" R"
        
        for j in range(len(arr)):
            column = [arr[i][j] for i in range(len(arr))]
            if column==column[::-1]:
                return str(j)+" C"
        
        return -1        
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        a = list()
        c = 0
        for i in range(0, n):
            X = list()
            for j in range(0, n):
                X.append(arr[c])
                c += 1
            a.append(X)
        ans = ob.pattern(a)
        print(ans)

# } Driver Code Ends