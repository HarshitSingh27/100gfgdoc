#User function Template for python3
class Solution:
    def MedianOfArrays(self, array1, array2):
        arr3=arr1+arr2
        arr3.sort()
        la3=len(arr3)
        median=0
        l=len(arr1)
        m=len(arr2)
        if (la3%2==0):
            median=(arr3[(l+m)//2-1]+arr3[(l+m)//2])/2;
            if median==int(median):
                return int(median)
            else:
                return median
        else:  
            median=arr3[(l+m)//2];
            return median    

#{ 
#  Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        m = input()
        arr1=[int(x) for x in input().split()]
        n = input()
        arr2=[int(x) for x in input().split()]
        
        
        ob = Solution()
        print(ob.MedianOfArrays(arr1,arr2))

# } Driver Code Ends