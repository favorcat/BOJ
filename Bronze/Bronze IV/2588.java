import java.util.Scanner;
public class Main {
    public static void main(String[]args){
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();
        String m = scan.next();
        scan.close();

        System.out.println(n*(m.charAt(2)-'0'));
        System.out.println(n*(m.charAt(1)-'0'));
        System.out.println(n*(m.charAt(0)-'0'));
        System.out.println(n*Integer.parseInt(m));
    }
}