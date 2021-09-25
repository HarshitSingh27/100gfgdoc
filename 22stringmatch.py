#User function Template for python3

class Solution:
    def repeatedStringMatch(self, A, B):
        copyA=A
        if A.count(B)>0:
            return 1
        else:
            c=1
            while(len(A)<len(B)):
                A=A+copyA
                c+=1
            if A.count(B)>0:
                return c
            A+=copyA
            c+=1
            if A.count(B)>0:
                return c
            else:
                return -1
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        A=input().strip()
        B=input().strip()
        obj = Solution()
        print(obj.repeatedStringMatch(A,B))
# } Driver Code Ends