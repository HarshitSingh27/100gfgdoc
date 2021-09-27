#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        dict={}
        presum=0
        maxlen=0
        for i in range(n):
            presum+=arr[i]
            if presum==0:
               maxlen=i+1
            if presum in dict:
               maxlen=max(maxlen,i-dict[presum])
            else:
               dict[presum]=i
        return maxlen        

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends