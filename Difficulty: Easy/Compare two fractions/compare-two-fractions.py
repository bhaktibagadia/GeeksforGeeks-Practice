#User function Template for python3
class Solution:
    def compareFrac (self, str):
        # code here
        str=str.split(",")
        t1=str[0].split('/')
        t2=str[1].split('/')
        num1=int(t1[0])/int(t1[1])
        num2=int(t2[0])/int(t2[1])
        if num1==num2:
            return 'equal'
        elif num1>num2:
            return str[0]
        else:
            return str[1][1:]
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import re

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        str = input()
        print(ob.compareFrac(str))

# } Driver Code Ends