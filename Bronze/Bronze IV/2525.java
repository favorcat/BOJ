import java.util.Scanner;

public class Main {
    public static void main(String[]args){
        Scanner scan = new Scanner(System.in);

        int h = scan.nextInt();
        int m = scan.nextInt();
        int t = scan.nextInt();

        m += t;
        h += m/60;
        m %= 60;
        h %= 24;

        System.out.println(h+" "+m);
    }
}