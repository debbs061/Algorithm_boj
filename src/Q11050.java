import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 이항계수 (Binomial Coefficient)
 */
public class Q11050 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        // n개 중에 k를 중복없이 뽑으려 한다.
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[][] dp = new int[N + 1][K + 1];

        // 2번 성질 (n == k)
        for (int i = 0; i <= K; i++) {
            dp[i][i] = 1;
        }

        // 2번 성질 (k == 0)
        for (int i = 0; i <= N; i++) {
            dp[i][0] = 1;
        }

        for (int i = 2; i <= N; i++) {
            for (int j = 1; j <= K; j++) {
                // 1번 성질 (i-1개 중에 j-1 을 뽑는 경우 수 + i-1개 중에 j개를 뽑는 경우 수)
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
            }
        }

        System.out.println(dp[N][K]);
    }
}
