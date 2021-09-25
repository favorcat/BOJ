import java.util.Scanner;

public class Main {
    public static void main(String[]args){
        Scanner scan = new Scanner(System.in);

        while(true){
            int n = scan.nextInt();
            int m = scan.nextInt();
            if (n == 0 && m==0) break;

            if (m%n==0) System.out.println("factor");
            else if (n%m==0) System.out.println("multiple");
            else System.out.println("neither");
        }
    }
}