#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        # your code here
        fibo=[0]*n
        if n==1:
            return [1]
        else:
            fibo[0]=1
            fibo[1]=1
        for i in range(2, n):
            fibo[i]=fibo[i-1]+fibo[i-2]
        return fibo   


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n=int(input())
        res = Solution().printFibb(n)
        for i in range (len(res)):
            print (res[i], end = " ") 
        print()
# } Driver Code Ends