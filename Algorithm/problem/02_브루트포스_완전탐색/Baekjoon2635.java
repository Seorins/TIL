package Algorithm;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Baekjoon2635 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int first_num = Integer.parseInt(br.readLine());

        ArrayList<Integer> best_list = new ArrayList<>();

        for (int second_num = 1; second_num <= first_num; second_num++) {
            ArrayList<Integer> list = new ArrayList<>();
            list.add(first_num);
            list.add(second_num);

            int n = 1;

            while (true) {
                int next = list.get(n - 1) - list.get(n);
                if (next < 0) break; 
                list.add(next);
                n++;
            }

            if (list.size() > best_list.size()) {
                best_list = list;
            }
        }

        System.out.println(best_list.size());
        for (int num : best_list) {
            System.out.print(num + " ");
        }
    }
}
