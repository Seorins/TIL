package Algorithm;
import java.io.*;

public class SWEA1961
{
    public static void main(String[] args) throws Exception
    {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      int T = Integer.parseInt(br.readLine());
      int N = Integer.parseInt(br.readLine());

      int[][] matrix = new int[N][N];


      for(int i=0; i<N; i++){  
        String[] input = br.readline().split(" ");
        int 
      }
      // String[][] input = br.readLine().split(" ");

      for(int i=0; i<N; i++){
        for(int j=0; j<N; j++){
          matrix[i][j] = Integer.parseInt(input[i][j]);
          System.out.println(matrix[i][j]);
        }
      }
    	
    }
}
