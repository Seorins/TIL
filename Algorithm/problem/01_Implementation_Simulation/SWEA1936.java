package Algorithm;
import java.io.*;

public class SWEA1936
{
    public static void main(String[] args) throws Exception
    {
    	
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	
    	String[] input = br.readLine().split(" ");
    	
    	int A = Integer.parseInt(input[0]);
    	int B = Integer.parseInt(input[1]);
    	
    	if(A==1 && B==3 || A==2 && B==1 || A==3 && B==2) {
    		System.out.println("A");
    	}
    	
    	else {
    		System.out.println("B");
    	}
    			
    	
     }
}
