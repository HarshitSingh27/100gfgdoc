#User function Template for python3

#Back-end complete function Template for Python 3

 
class Solution:
    def maxCandy(self, height, n): 
        ans=0
        i=0
        j=n-1
        
        while(i<j):
            if(height[i]<height[j]):
                ans=max(ans,(j-i-1)*(height[i]))
                i+=1
            if(height[i]>height[j]):
                ans=max(ans,(j-i-1)*(height[j]))
                j-=1
            if(height[i]==height[j]):
                ans=max(ans,(j-i-1)*(height[i]))
                i+=1
                j-=1
        return ans            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.maxCandy(arr,n))



# } Driver Code Ends