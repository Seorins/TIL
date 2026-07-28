package Algorithm;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Baekjoon2669 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        boolean[][] grid = new boolean[101][101];

        for (int k = 0; k < 4; k++) {
            String[] input = br.readLine().split(" ");
            int x1 = Integer.parseInt(input[0]);
            int y1 = Integer.parseInt(input[1]);
            int x2 = Integer.parseInt(input[2]);
            int y2 = Integer.parseInt(input[3]);

            for (int i = x1; i < x2; i++) {
                for (int j = y1; j < y2; j++) {
                    grid[i][j] = true;
                }
            }
        }

        int sum = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid.length; j++) {
                if (grid[i][j] == true) {
                    sum++;
                }
            }
        }

        System.out.println(sum);
    }
}
