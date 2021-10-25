// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
class Solution
{
    public:
    //Function to find largest rectangular area possible in a given histogram.
    vector<long long> leftSmaller(long long arr[], int n){
        stack<long long> s;
        vector<long long> res(n);
        for(long long i=0; i<n; i++){
            while(!s.empty() && arr[s.top()]>=arr[i]){
                s.pop();
            }
            if(s.empty()){
                res[i] = -1;
            } else {
                res[i] = s.top();
            }
            s.push(i);
        }
        return res;
    }
    
    vector<long long> rightSmaller(long long arr[], int n){
        stack<long long> s;
        vector<long long> res(n);
        for(long long i=n-1; i>=0; i--){
            while(!s.empty() && arr[s.top()]>=arr[i]){
                s.pop();
            }
            if(s.empty()){
                res[i] = n;
            } else {
                res[i] = s.top();
            }
            s.push(i);
        }
        return res;
    }
    long long getMaxArea(long long arr[], int n)
    {
        // Your code here
        long long ans = 0;
        vector<long long> left = leftSmaller(arr, n);
        vector<long long> right = rightSmaller(arr, n);
        for(long long i=0; i<n; i++){
            long long mx = (right[i]-left[i]-1)*arr[i];
            ans = max(ans, mx);
        }
        return ans;
    }
};


// { Driver Code Starts.

int main()
 {
    long long t;

    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        
        long long arr[n];
        for(int i=0;i<n;i++)
            cin>>arr[i];
        Solution ob;
        cout<<ob.getMaxArea(arr, n)<<endl;
    
    }
	return 0;
}
  // } Driver Code Ends