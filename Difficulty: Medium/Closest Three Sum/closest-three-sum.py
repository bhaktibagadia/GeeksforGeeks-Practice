#User function Template for python3

# arr    : list of integers denoting the elements of the array
# target : as specified in the problem statement

class Solution:
    def threeSumClosest (self, arr, target):
    # Your Code Here
        arr.sort()
        diff=float('inf')
        ans=-1
        for i in range(len(arr)):
            ptr1=i+1
            ptr2=len(arr)-1
            while ptr1<ptr2:
                summ=arr[i]+arr[ptr1]+arr[ptr2]
                if summ==target:
                    return target
                currentdiff=abs(summ-target)    
                if currentdiff<diff or (currentdiff==diff and summ>ans):
                    diff=currentdiff
                    ans=summ
                if summ>target:
                    ptr2-=1
                else:
                    ptr1+=1
        return ans           


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.threeSumClosest(A, k))

# } Driver Code Ends