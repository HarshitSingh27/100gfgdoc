// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution{
public:
	using ll = long long;
    const ll mod = 1e9+7;
	int TotalAnimal(long long int N){
	    // Code here
	    //fibonacci
	   // companinion matrix [[1,1],[1,0]]
	   //fn = A^n-1 * f1;//f1= 1,f0 =0
	   //modular multiplication
	   ll a[2][2] = {{1,1},{1,0}};
	   ll ans = powerMatrix(a,N);
	   return (int)ans;
	}
	long long powerMatrix(ll a[][2],long long b){
        ll res[2][2] = {{1,0},{0,1}}; 
        while(b>0){
            if(b%2 != 0){
                //res = res*a%mod;
                multiply(res,a);
            }
            b >>= 1;//b /= 2
            //a = a*a%mod;
            multiply(a,a);
        }
       return res[0][0];
	}
	void multiply(ll a[][2],ll b[][2]){
	    ll ans[2][2];
	    for(int i=0; i<2; i++){
	        for(int j=0; j<2; j++){
	            ans[i][j] = 0;
	            for(int k=0; k<2; k++){
	                ans[i][j] = (ans[i][j]+a[i][k]*b[k][j]%mod)%mod;
	            }
	        }
	    }
	    for(int i=0; i<2; i++){
	        for(int j=0; j<2; j++){
	            a[i][j] = ans[i][j];
	        }
	    }
	}
};

// { Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		long long int N;
		cin >> N;
		Solution ob;
		int ans = ob.TotalAnimal(N);
		cout << ans << "\n";
	}
	return 0;
}  // } Driver Code Ends