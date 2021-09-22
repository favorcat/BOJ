import java.util.Scanner;

public class Main {
    public static void main(String[]args){
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();
        int ans = 1;
        while (n != 0){
            ans *= n;
            n--;
        }
        System.out.println(ans);
    }
}