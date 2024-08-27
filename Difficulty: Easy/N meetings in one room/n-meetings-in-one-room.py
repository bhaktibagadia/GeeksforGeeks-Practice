#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        timings = [[0, 0] for _ in range(n)]
        meetings= 0
        for i in range(n):
            timings[i][0] = start[i]
            timings[i][1] = end[i]
        timings.sort(key = lambda x:x[1])
        end = 0
        for timing in timings:
            start = timing[0]
            if start>end:
                meetings+=1
                end = timing[1]
        return meetings        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends