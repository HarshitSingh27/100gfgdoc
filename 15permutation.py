#User function Template for python3
from itertools import permutations as per
class Solution:
    def uniquePerms(self, arr, n):
        ans_lis = []
        set_ans = set(per(arr))
        for i in set_ans:
            ans_lis.append(i)
        return sorted(ans_lis)
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        res = ob.uniquePerms(arr,n)
        for i in range(len(res)):
            for j in range(n):
                print(res[i][j],end=" ")
            print()
# } Driver Code Ends