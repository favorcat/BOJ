import java.util.Scanner;
public class Main {
    public static void main(String[]args){
        Scanner scan = new Scanner(System.in);

        long a = scan.nextLong();
        long b = scan.nextLong();
        long c = scan.nextLong();
        System.out.println(cal(a % c, b, c));
    }

    private static long cal(long a, long b, long c){
        if(b==1) return a;
        long temp = cal(a, b/2, c) % c;
        if(b % 2 == 0) return (temp * temp) % c;
        else return (((temp * temp) % c) * a) % c;
    }
}