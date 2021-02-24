import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * @FileName : Q2675
 * @Link : https://www.acmicpc.net/problem/2675
 * @Date : 2021/02/25
 */
public class Q2675 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int t = Integer.parseInt(br.readLine());
        String ans[] = new String[t];

        for (int k = 0; k < t; k++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            String tmp = st.nextToken();
            String newTmp = "";
            for (int i = 0; i < tmp.length(); i++) {
                for (int j = 0; j < n; j++) {
                    newTmp += tmp.charAt(i);
                }
            }
            ans[k] = newTmp;
        }

        for (String tmp : ans) {
            System.out.println(tmp);
        }
    }
}
