import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Q10773 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int k = Integer.parseInt(br.readLine());
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < k; i++) {

            int number = Integer.parseInt(br.readLine());
            if (number == 0) {
                stack.pop();
            } else {
                stack.push(number);
            }
        }
        int sum = 0;
        for (int o : stack) {
            sum += o;
        }
        System.out.println(sum);
    }
}