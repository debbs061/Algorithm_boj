import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * @FileName : Q1152
 * @Link : https://www.acmicpc.net/problem/1152
 * @Date : 2021/02/25
 */
public class Q1152 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        System.out.println(st.countTokens());
    }
}
