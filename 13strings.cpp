// { Driver Code Starts
//Initial template for C++

#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
//User function template for C++
class Solution{
  public:
    bool isInterleave(string A, string B, string C) {
        int a = A.length(), b = B.length(), c = C.length();
        if(a+b != c) return false;
        bool dp[a+1][b+1];
        dp[0][0] = true;
        for(int i=1; i<=a; i++)
            dp[i][0] = (dp[i-1][0] && A[i-1] == C[i-1]);
        for(int j=1; j<=b; j++) 
            dp[0][j] = (dp[0][j-1] && B[j-1] == C[j-1]);
        for(int i=1; i<=a; i++) {
            for(int j=1; j<=b; j++) {
                dp[i][j] = (dp[i-1][j] && A[i-1] == C[i+j-1]) ||
                            (dp[i][j-1] && B[j-1] == C[i+j-1]);
            }
        }
        return dp[a][b];
    }
};


// { Driver Code Starts.
int main() {
	int t;
	cin>>t;
	while(t--)
	{
		string a,b,c;
		cin>>a;
		cin>>b;
		cin>>c;
		Solution obj;
		cout<<obj.isInterleave(a,b,c)<<endl;
	}
	// your code goes here
	return 0;
}  // } Driver Code Ends