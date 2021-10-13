// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution{

	public:
	int findK(vector<vector<int>> &a, int n, int m, int k) {
        int left=0;   //flow controls
        int right=m-1;
        int top=0;
        int bottom=n-1;
        int dir=0;
        
        // dir==0 left->right
        // dir==1 top->bottom
        // dir==2 right->left
        // dir==3 bottom->top
        
        while(top<=bottom && left<=right){
            if(dir==0){
                for(int i=left;i<=right;i++){
                    k--;
                    if(k==0){
                        return a[top][i];  
                    }
                }
                top++;
            }
            
            if(dir==1){
                for(int i=top;i<=bottom;i++){
                    k--;
                    if(k==0){
                    return a[i][right];  
                    }
                }
                right--;
            }
            
            if(dir==2){
                for(int i=right;i>=left;i--){
                    k--;
                    if(k==0){
                        return a[bottom][i];
                    }
                }
                bottom--;
            }
            
            if(dir==3){
                for(int i=bottom;i>=top;i--){
                    k--;
                    if(k==0){
                        return a[i][left];
                    }
                }
                left++;
            }
            
            dir=(dir+1)%4;
        }
        return -1;
    }

};

// { Driver Code Starts.

int main()
{
    int T;
    cin>>T;
  
    while(T--)
    {
        int n,m;
        int k=0;
        //cin>>k;
        cin>>n>>m>>k;
        vector<vector<int>> a(n, vector<int>(m, 0));
        
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                cin>>a[i][j];
            }
        }

        Solution obj;

        cout<< obj.findK(a, n, m, k) << "\n";
        
       
    }
}  // } Driver Code Ends