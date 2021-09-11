import java.util.Scanner;

public class Main {
    public static void main(String[]args){
        Scanner scan = new Scanner(System.in);

        int k = scan.nextInt();
        int n = scan.nextInt();
        int m = scan.nextInt();

        int ans = k*n-m;
        if (ans <= 0) ans = 0;
        System.out.print(ans);
    }
}
