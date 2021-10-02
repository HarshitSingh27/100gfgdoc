#User function Template for python3

class Solution: 
    def candies(self, m,n): 
        return int((m-1)*(n-1)/2) 

#{ 
#  Driver Code Starts
#Initial Template for Python 3
	
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
    	arr = list(map(int, input().strip().split()))
    	m = arr[0]
    	n = arr[1]
    	obj = Solution()
    	print(obj.candies(m,n)) 



# } Driver Code Ends