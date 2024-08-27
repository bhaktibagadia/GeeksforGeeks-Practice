#User function Template for python3
import math
class Solution:
    def jugglerSequence(self, n):
        # code here
        a = n
        ans = []
        ans.append(n)
        while a!=1:
            if a%2 == 0:
                b = int(math.floor(math.sqrt(a)))
            else:
                b = int(math.floor(math.sqrt(a)*math.sqrt(a)*math.sqrt(a)))
            ans.append(b)    
            a = b
        return ans    
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        arr = ob.jugglerSequence(n)
        for i in (arr):
            print(i, end=" ")
        print()

# } Driver Code Ends