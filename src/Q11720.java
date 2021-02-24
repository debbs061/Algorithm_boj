import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * @FileName : 11720
 * @Link : https://www.acmicpc.net/problem/11720
 * @Date : 2021/02/25
 */
public class Q11720 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String tmp = br.readLine();
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += tmp.charAt(i) - '0';
        }
        System.out.println(sum);
    }
}
