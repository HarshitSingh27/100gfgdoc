#User function Template for python3
class Solution:
	def maxSubstring(self, S):
	    sweep = 0
	    ans = -1
	    for i in S:
	        
	        if i == '0':
	            sweep += 1
	        else:
	            sweep -= 1
	            
	        ans = max(ans, sweep)
	        if sweep < 0:
	            sweep = 0
	            
	    return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.maxSubstring(s)
		print(answer)

# } Driver Code Ends