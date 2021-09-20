import java.util.Scanner;

public class Main {
    public static void main(String[]args){
        Scanner scan = new Scanner(System.in);

        long n = scan.nextLong();
        long m = scan.nextLong();
        if (n==m) System.out.println(1);
        else System.out.println(0);
    }
}