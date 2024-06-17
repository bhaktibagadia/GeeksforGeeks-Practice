from collections import Counter
class Solution:
    def duplicates(self, arr, n): 
        # code here
        freq=Counter(arr)
        ans=[]
        for i in freq:
            if freq[i]>1:
                ans.append(i)
        if ans:
            return sorted(ans)
        return [-1]    





#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends