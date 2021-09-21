import java.util.Scanner;

public class Main {
    public static void main(String[]args){
        Scanner scan = new Scanner(System.in);

        int m = scan.nextInt();
        int d = scan.nextInt();
        if ((m < 2) || (m == 2 && d < 18)) System.out.println("Before");
        else if (m==2 && d==18) System.out.println("Special");
        else System.out.println("After");
    }
}