#User function Template for python3

class Solution:
    def maxFrequency(self, S):
       # code here
       st=""
       n=len(S)
       for i in S:
           st+=i
           if (st==S[n-len(st):]):
               break
       cnt=0
       for i in range(n-len(st)+1):
           if S[i:i+len(st):]==st:
               cnt+=1
       return cnt
#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        Str = input()
        obj = Solution()

        print(obj.maxFrequency(Str))

# } Driver Code Ends