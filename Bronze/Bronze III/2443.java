import java.util.Scanner;
public class Main {
    public static void main(String[]args){
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();
        int idx = 2 * n - 1;
        for(int i=n; i>=1; i--){
            for(int j=n; j>i; j--) System.out.print(" ");
            for(int k=0; k<idx; k++) System.out.print("*");
            idx-=2;
            System.out.println();
        }
    }
}