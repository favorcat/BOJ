import java.util.Scanner;
public class Main {
    public static void main(String[]args){
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();
        boolean[] arr = new boolean[101];
        int cnt = 0;

        for(int i=0; i<n; i++){
            int seat = scan.nextInt();
            if (arr[seat]) cnt++;
            else arr[seat] = true;
        }
        System.out.println(cnt);
    }
}