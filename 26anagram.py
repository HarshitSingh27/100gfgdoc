#User function Template for python3
class Solution:

	def search(self, pat, txt):
        n, m, ans = len(txt), len(pat), 0
        ar, br = [0]*26, [0]*26
    
        for i in range(m):
            ar[ord(pat[i]) - 97] += 1
            br[ord(txt[i]) - 97] += 1
    
        for i in range(m, n):
            if ar == br: ans += 1
            br[ord(txt[i]) - 97] += 1
            br[ord(txt[i-m]) - 97] -= 1
    
        return ans+1 if ar == br else ans
	

#{ 
#  Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        txt=input().strip()
        pat=input().strip()
        ob = Solution()
        ans = ob.search(pat, txt)
        print(ans)
        tc=tc-1
# } Driver Code Ends