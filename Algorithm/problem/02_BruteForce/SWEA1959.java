package Algorithm;
import java.io.*;

public class SWEA1959
{
    public static void main(String[] args) throws Exception
    {
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for(int t=0; t<T; t++){
            
            String[] num = br.readLine().split(" ");
            int N = Integer.parseInt(num[0]);
            int M = Integer.parseInt(num[1]);

            String[] A = br.readLine().split(" ");
            String[] B = br.readLine().split(" ");
            int[] Ai = new int[N];
            int[] Bj = new int[M];
            
            for(int j=0; j<N; j++){
                Ai[j] = Integer.parseInt(A[j]);
            }

            for(int j=0; j<M; j++){
                Bj[j] = Integer.parseInt(B[j]);
            }

            int[] shortarr = Ai;
            int[] longarr = Bj;

            if(Ai.length > Bj.length){
                shortarr = Bj;
                longarr = Ai;
            }
            
            int sum_max = 0;
            
            for(int i=0; i<=longarr.length-shortarr.length; i++) {
                int sum =0;
                for(int j=0; j<shortarr.length; j++){
                    sum += shortarr[j]*longarr[i+j];
               }
               sum_max = Math.max(sum_max, sum);
            }
            System.out.println("#" + (t + 1) + " " + sum_max);
        }
    }
}