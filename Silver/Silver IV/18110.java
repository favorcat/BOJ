import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import java.util.Arrays;
public class Main {
    public static void main(String[]args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int testcase = Integer.parseInt(br.readLine());
        int[] arr = new int[testcase];

        for(int i=0; i<testcase; i++)   arr[i] = Integer.parseInt(br.readLine());
        Arrays.sort(arr);

        int n = (int)Math.round(testcase*0.15);
        double sum = 0;
        for(int i=n; i<testcase-n; i++) sum += arr[i];
        System.out.println((int)Math.round(sum/(testcase-n*2)));
    }
}