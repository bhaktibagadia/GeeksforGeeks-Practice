#User function Template for python3

class Solution:
    def InternalCount(self, p, q, r):
        #code here
        def gcd(a, b):
            while b:
                temp=b
                b=a%b
                a=temp
            return a
        
        area2=abs(p[0]*(q[1]-r[1])+q[0]*(r[1]-p[1])+r[0]*(p[1]-q[1]))
        area=area2//2
        bpq=gcd(abs(p[0]-q[0]), abs(p[1]-q[1]))
        bqr=gcd(abs(q[0]-r[0]), abs(q[1]-r[1]))
        brp=gcd(abs(r[0]-p[0]), abs(r[1]-p[1]))
        boundary=bpq+bqr+brp
        internal=area-(boundary//2)+1
        return internal


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        p=[0]*2
        q=[0]*2
        r=[0]*2
        p[0],p[1],q[0],q[1],r[0],r[1]=map(int,input().strip().split(" "))
        ob=Solution()
        ans=ob.InternalCount(p,q,r);
        print(ans)
# } Driver Code Ends