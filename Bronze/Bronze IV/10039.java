import java.util.Scanner;
public class Main {
    public static void main(String[]args){
        Scanner scan = new Scanner(System.in);

        int sum = 0;
        for(int i=0; i<5; i++){
            int n = scan.nextInt();
            if (n<40) n = 40;
            sum += n;
        }
        scan.close();
        System.out.println(sum / 5);
    }
}