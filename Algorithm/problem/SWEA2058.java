package Algorithm;
import java.io.*;

public class swea2058
{
    public static void main(String[] args) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int sum = 0;

        while(N > 0){ 
            sum += N%10; 
            N = N/10 ; 
        }

        System.out.println(sum);
    	
    }
}
