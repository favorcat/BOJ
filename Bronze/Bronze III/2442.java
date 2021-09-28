import java.util.Scanner;
public class Main {
    public static void main(String[]args){
        Scanner scan = new Scanner(System.in);

        int idx = 1;
        int n = scan.nextInt();
        for(int i=1; i<=n; i++){
            for(int j=n; j>i; j--) System.out.print(" ");
            for(int k=0; k<idx; k++) System.out.print("*");
            idx+=2;
            System.out.println();
        }
    }
}