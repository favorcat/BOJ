import java.util.Scanner;

public class Main {
    public static void main(String[]args){
        Scanner scan = new Scanner(System.in);

        int D = scan.nextInt();
        int H = scan.nextInt();
        int W = scan.nextInt();

        double x = Math.sqrt(Math.pow(D, 2) / (Math.pow(H, 2) + Math.pow(W, 2)));
        System.out.print((int)Math.floor(H*x)+" ");
        System.out.print((int)Math.floor(W*x));
    }
}