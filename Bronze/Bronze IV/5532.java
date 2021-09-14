import java.util.Scanner;

public class Main {
    public static void main(String[]args){
        Scanner scan = new Scanner(System.in);

        int l = scan.nextInt();
        double a = scan.nextDouble();
        double b = scan.nextDouble();
        double c = scan.nextDouble();
        double d = scan.nextDouble();

        int total = Math.max((int)Math.ceil(a/c), (int)Math.ceil(b/d));
        System.out.println(l-total);
    }
}