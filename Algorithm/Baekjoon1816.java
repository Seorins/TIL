package Algorithm;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Baekjoon1816 {
    public static void main(String[] args) throws Exception {

      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

      int input = Integer.parseInt(br.readLine());

      for(int i=0; i < input; i++){
          long num = Long.parseLong(br.readLine());
          boolean bool = true;

            for(int j=2; j<1000001; j++){
              if(num % j == 0){
                bool = false;
              }
              if(i==1000000){
                bool = true;
              }
            }
              if(bool==false){
                System.out.println("NO");
              }
              else{
                System.out.println("YES");
              }
          }
  }
}
