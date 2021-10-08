import java.util.Scanner;
public class Main {
    public static void main(String[]args){
        Scanner scan = new Scanner(System.in);

        String s = scan.next();
        String[] arr = s.split(",");
        int result = 0;

        for (String value : arr)
            result += Integer.parseInt(value);
        System.out.println(result);
    }
}