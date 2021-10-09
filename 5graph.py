#User function Template for python3
class Solution:
    def __init__(self):
        self.ans0 = 0
        self.ans1 = []
        self.ans2 = []
        self.ans3 = []
        self.rd1 = [0]*1100
        self.wt2 = [0]*1100
        self.cd3 = [0]*1100
        self.f_ans = []
        
    def dfs(self, w):
        if (self.cd3[w] == 0):
            return w
        if (self.wt2[w] < self.ans0):
            self.ans0 = self.wt2[w]
        return self.dfs(self.cd3[w])
        
    def solve(self, n, p ,a, b, d):
            
        i = 0
        
        while i < p:
            x = a[i]
            y = b[i]
            z = d[i]
            
            self.cd3[x] = y
            self.wt2[x] = z
            self.rd1[y] = x
            i += 1
            
        for j in range(1, n + 1):
            if self.rd1[j] == 0 and self.cd3[j]:
                 
                self.ans0 = 1000000000
                w = self.dfs(j)
                
                self.ans1.append(j)
                self.ans2.append(w)
                self.ans3.append(self.ans0)
                
        for i in range(len(self.ans1)):
            self.f_ans.append([self.ans1[i], self.ans2[i], self.ans3[i]])
            
        return self.f_ans 
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        
        n,p = map(int,input().strip().split())
        a = []
        b = []
        d = []
        for i in range(p):
            x,y,z = map(int,input().strip().split())
            a.append(x)
            b.append(y)
            d.append(z)
            
        ob = Solution()
        ans = ob.solve(n, p, a, b, d)
        print(len(ans))
        for i in ans:
            print(str(i[0])+" "+str(i[1])+" "+str(i[2]))


# } Driver Code Ends