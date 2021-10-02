import java.util.Scanner;
public class Main {
    public static void main(String[]args){
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();
        n = 1000-n;
        int cnt = 0;
        int[] arr = {500, 100, 50, 10, 5, 1};

        for(int i=0; i<6; i++){
            cnt += n / arr[i];
            n %= arr[i];
        }
        System.out.println(cnt);
    }
}