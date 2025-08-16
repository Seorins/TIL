package Algorithm;
import java.io.*;
import java.util.Arrays;

public class SWEA2063
{
    public static void main(String[] args) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String[] score = br.readLine().split(" ");
        int[] scores = new int[score.length];

        for(int i=0; i<score.length; i++){
            scores[i] = Integer.parseInt(score[i]);
        }

        Arrays.sort(scores);

        System.out.println(scores[N/2]);

        // 한 줄짜리 배열 변환 방법
        // int[] arr = Arrays.stream(br.readLine().split(" "))
        //           .mapToInt(Integer::parseInt)
        //           .toArray();
        
    }
}
