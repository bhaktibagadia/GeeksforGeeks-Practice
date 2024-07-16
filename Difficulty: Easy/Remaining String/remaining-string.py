#User function Template for python3
class Solution:
	def printString(self, s, ch, count):
		# code here
		i=0
		while count>0 and i<len(s):
		    if s[i]==ch:
		        count-=1
		    i+=1
		if i<len(s):
		    return s[i:]
		return ""    
		      


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()
        ch = input()[0]
        count = int(input())
        ob = Solution()
        answer = ob.printString(s, ch, count)

        print(answer)

# } Driver Code Ends