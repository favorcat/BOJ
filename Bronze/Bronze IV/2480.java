import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[]args){
        Scanner scan = new Scanner(System.in);

        int result = 0;
        int a = scan.nextInt();
        int b = scan.nextInt();
        int c = scan.nextInt();
        int[] arr = {a,b,c};
        Arrays.sort(arr);

        if (arr[0] == arr[1] && arr[1] == arr[2])
            result = 10000+arr[0]*1000;
        else{
            if (arr[0] != arr[1] && arr[1] != arr[2] && arr[0] != arr[2])
                result = arr[2]*100;
            else result = 1000+arr[1]*100;
        }
        System.out.println(result);
    }
}