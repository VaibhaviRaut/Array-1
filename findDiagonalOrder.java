//TC: O(mxn) as we traverse through the elements in matrix
//SP\C: O(n) as we are storing n elements
//Leetcode: Success!
//Problems: switching from Python to Java

class Solution {
    public int[] findDiagonalOrder(int[][] matrix) {
        //Sanity check
        if(matrix==null || matrix.length==0) return new int[0];
        
        // Initialize the rows and cols length
        int m = matrix.length;
        int n = matrix[0].length;
        
        //Initialize resultant matrix
        int[] res = new int[m*n];
        
        int i = 0; int r = 0; int c = 0; int dir = 1;
        while(i<m*n){
            // initialize resultant array
            
            res[i] = matrix[r][c];
            // Upward direction
            if(dir==1){
                // check if the at the last column
                if(c==n-1){
                    r++;
                    dir = -1;
                }
                // check if at first row
                else if(r==0){
                    c++;
                    dir = -1;
                }
                else{
                    r--;
                    c++;
                }
            }
            // Downward direction
            else{
                // check if the at the last row
                if(r==m-1){
                    c++;
                    dir = 1;
                }
                // check if at first column
                else if(c==0){
                    r++;
                    dir = 1;
                }
                else{
                    r++;
                    c--;
                }
            }
            i++;
        }
        return res;
    }
}
