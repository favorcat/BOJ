import java.util.Scanner;
public class Main {
    public static void main(String[]args){
        Scanner scan = new Scanner(System.in);

        int a, b, c, ans;
        a = scan.nextInt();
        b = scan.nextInt();
        c = scan.nextInt();
        scan.close();

        if (c-b < 1) ans = -1;
        else ans = a / (c-b) + 1;
        System.out.println(ans);
    }
}