package Java;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class StringArrayToIntArrayExamples {

    public static void main(String[] args) throws Exception {

        // 1. 기본 for문을 사용하여 String[] → int[]
        String[] str1 = {"10", "20", "30"};
        int[] arr1 = new int[str1.length];
        for (int i = 0; i < str1.length; i++) {
            arr1[i] = Integer.parseInt(str1[i]);
        }
        System.out.println("1. for문 결과: " + Arrays.toString(arr1));


        // 2. Arrays.stream() 사용하여 한 줄로 변환
        String[] str2 = {"1", "2", "3", "4"};
        int[] arr2 = Arrays.stream(str2)
                           .mapToInt(Integer::parseInt)
                           .toArray();
        System.out.println("2. stream 결과: " + Arrays.toString(arr2));


        // 3. BufferedReader로 입력받아 String[] → int[]
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("3. 공백으로 구분된 숫자 입력: ");
        String[] input = br.readLine().split(" ");
        int[] arr3 = new int[input.length];
        for (int i = 0; i < input.length; i++) {
            arr3[i] = Integer.parseInt(input[i]);
        }
        System.out.println("입력 받은 숫자 배열: " + Arrays.toString(arr3));


        // 4. ArrayList<Integer>에 변환하여 저장
        String[] str4 = {"100", "200", "300"};
        ArrayList<Integer> list = new ArrayList<>();
        for (String s : str4) {
            list.add(Integer.parseInt(s));
        }
        System.out.println("4. ArrayList 결과: " + list);
    }
}
