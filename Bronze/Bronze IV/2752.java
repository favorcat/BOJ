import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[]args){
        Scanner scan = new Scanner(System.in);

        int[] arr = new int[3];
        for(int i=0; i<3; i++)  arr[i] = scan.nextInt();
        Arrays.sort(arr);
        for(int i : arr)    System.out.print(i+" ");
    }
}