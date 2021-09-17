import java.util.Scanner;

public class Main {
    public static void main(String[]args){
        Scanner scan = new Scanner(System.in);

        int S = 0;
        int T = 0;
        for(int i=0; i<4; i++) S += scan.nextInt();
        for(int i=0; i<4; i++) T += scan.nextInt();

        if (S == T) System.out.println(S);
        else System.out.println(Math.max(S, T));
    }
}