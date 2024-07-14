#User function Template for python3

class Solution:
    def segregate0and1(self, arr):
        # code here
        count0, count1=0,0
        for el in arr:
            if el==0:
                count0+=1
            else:
                count1+=1
        for i in range(count0):
            arr[i]=0
        for i in range(count0, count1+count0):
            arr[i]=1
        return arr    


#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = list(map(int, input().strip().split()))

        obj = Solution()
        obj.segregate0and1(arr)

        print(*arr)

# } Driver Code Ends