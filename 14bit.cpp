// { Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
//User function Template for C++

class Solution
{
    public:
    //Function to swap odd and even bits.
   unsigned int swapBits(unsigned int n) {
    for (int i = 0; i < 32; i += 2) {
        bool b1 = (n >> i) & 1, b2 = (n >> (i + 1)) & 1;
        if (b2)n |= (1 << i);
        else n &= ~(1 << i);
        if (b1)n |= (1U << (i + 1));
        else n &= ~(1U << (i + 1));
    }
    return n;
}
};

// { Driver Code Starts.

// Driver code
int main()
{
	int t;
	cin>>t;//testcases
	while(t--)
	{
		unsigned int n;
		cin>>n;//input n
		
		Solution ob;
		//calling swapBits() method
		cout << ob.swapBits(n) << endl;
	}
	return 0;
}  // } Driver Code Ends