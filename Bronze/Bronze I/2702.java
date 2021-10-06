import java.util.Scanner;
public class Main {
    public static void main(String[]args){
        Scanner scan = new Scanner(System.in);

        int testcase = scan.nextInt();
        for(int i=0; i<testcase; i++){
            int a = scan.nextInt();
            int b = scan.nextInt();
            int c = gcd(a, b);

            System.out.print(a * b / c + " ");
            System.out.println(c);
        }
    }
    public static int gcd(int a, int b){
        if(a % b == 0) return b;
        return gcd(b, a % b);
    }
}