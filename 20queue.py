#User function Template for python3

class MyQueue:
    def __init__(self):
        self.front = self.rear = 0
        self.arr = [0] * (10 ** 5)

    def push(self, x):
        self.arr[self.rear], self.rear = x, self.rear + 1
        
    def pop(self):
        if self.rear <= self.front: return -1
        t, self.front = self.arr[self.front], self.front + 1
        return t

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   

# } Driver Code Ends