#User function Template for python3

class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        i, j = 0 , 0
        ans=[]
        while i<n or j<m:
            if j>=m:
                ans.append(arr1[i])
                i+=1
            elif i>=n:
                ans.append(arr2[j])
                j+=1
            else:
                if arr1[i]>arr2[j]:
                    ans.append(arr2[j])
                    j+=1
                else:
                    ans.append(arr1[i])
                    i+=1
        return ans[k-1]   
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m, k = sz[0], sz[1], sz[2]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement( a, b, n, m, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends