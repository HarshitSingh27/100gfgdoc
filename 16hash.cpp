// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;



 // } Driver Code Ends

class Solution{
  public:
    vector <int> countDistinct (int A[], int n, int k){
       unordered_map<int,int> mpp;//create a map
       for(int i=0;i<k;i++){
           mpp[A[i]]++;   //increment values for the values of map for size k window
       }
       vector<int> res;
       res.push_back(mpp.size()); //push the size so that we get unique no. of ele.
       for(int i=k;i<n;i++){
           mpp[A[i-k]]--;  //decrement initial value
           if(mpp[A[i-k]]==0){
               mpp.erase(A[i-k]); //erase start values 
           }
           mpp[A[i]]++;
           res.push_back(mpp.size());  //push the size for each window.
       }
       return res;
    }
};

// { Driver Code Starts.
int main()
{
    int t;
    cin >> t;
    while (t--)
    {

        int n, k;
        cin >> n >> k;
        int a[n];
        for (int i = 0; i < n; i++) 
        	cin >> a[i];
        Solution obj;
        vector <int> result = obj.countDistinct(a, n, k);
        for (int i : result) 
        	cout << i << " ";
        cout << endl;
    }
    return 0;
}  // } Driver Code Ends