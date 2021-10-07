class Solution:
    
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V, adj):
		vis = [0]*V
		
		def dfs(cur, parent):
		    vis[cur] = 1
		    
		    for i in adj[cur]:
		        if not vis[i]:
		            if dfs(i, cur): return True
		        elif i != parent:
		            return True
		            
		    return False
		
		for i in range(V):
		    if not vis[i]:
		        if dfs(i, -1): return True
		        
		return False
		#Code here

#{ 
#  Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends