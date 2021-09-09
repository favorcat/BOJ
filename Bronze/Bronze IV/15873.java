import java.util.Scanner;
public class Main {
    public static void main(String[]args){
        Scanner scan = new Scanner(System.in);

        String n = scan.next();
        int sum = 0;
        int x = 0;

        for(int i=0; i<n.length(); i++){
            if (n.charAt(i) == '0'){
                sum -= x;
                x *= 10;
            }
            else x = n.charAt(i) - 48;
            sum += x;
        }
        System.out.println(sum);
    }
}