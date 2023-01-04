import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int target;
        Scanner sc = new Scanner(System.in);
        target = sc.nextInt();

        for (int i = 2; i <= target; i++){
            while(target % i == 0){
                System.out.println(i);
                target /= i;
            }
            if (target == 1){
                break;
            }
        }
    }
}
