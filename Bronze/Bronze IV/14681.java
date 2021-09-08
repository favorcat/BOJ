import java.util.Scanner;
public class Main {
    public static void main(String[]args){
        Scanner scan = new Scanner(System.in);

        int x, y;
        int ans = 0;
        x = scan.nextInt();
        y = scan.nextInt();

        if (x>0 && y>0) ans = 1;
        if (x<0 && y>0) ans = 2;
        if (x<0 && y<0) ans = 3;
        if (x>0 && y<0) ans = 4;
        System.out.println(ans);
    }
}