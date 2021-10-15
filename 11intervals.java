// { Driver Code Starts
import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        while(T-->0)
        {
            int n = Integer.parseInt(br.readLine().trim());
            String[] s = br.readLine().trim().split(" ");
            int[][] Intervals = new int[n][2];
            int j = 0;
            for(int i = 0; i < n; i++){
                Intervals[i][0] = Integer.parseInt(s[j]);
                j++;
                Intervals[i][1] = Integer.parseInt(s[j]);
                j++;
            }
            Solution obj = new Solution();
            int[][] ans = obj.overlappedInterval(Intervals);
            for(int i = 0; i < ans.length; i++){
                for(j = 0; j < ans[i].length; j++){
                    System.out.print(ans[i][j] + " ");
                }
            }
            System.out.println();
        }
    }
}
// } Driver Code Ends


class Solution
{
   public int[][] overlappedInterval(int[][] arr)
   {
       // Code here
       Arrays.sort(arr,new Comparator<int[]>()
       {
           public int compare(int[] a,int[] b)
           {
               if(a[0]==b[0])
               return a[1]-b[1];
               return a[0]-b[0];
           }
       });
       ArrayList<Integer> ar = new ArrayList<Integer>();
       int s=arr[0][0];
       int e=arr[0][1];
       for(int i=0;i<arr.length;i++)
       {
           if(e<arr[i][0])
           {
               ar.add(s);
               ar.add(e);
               s = arr[i][0];
               e = arr[i][1];
           }
           else
           {
               e=Math.max(e,arr[i][1]);
           }
       }
       ar.add(s);
       ar.add(e);
      // System.out.println(ar.size());
       int res[][] = new int[ar.size()/2][2];
       int c=0;
       for(int i=0;i<ar.size();i+=2)
       {
           res[c][0]=ar.get(i);
           res[c][1]=ar.get(i+1);
           c++;
       }
       return res;
   }
}