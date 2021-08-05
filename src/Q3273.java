import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Q3273 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        int a[] = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }
        int x = Integer.parseInt(br.readLine());
        int ans = 0;
        int sum = 0;
        int start = 0;
        int end = n-1;
        Arrays.sort(a);
        while (start < end) {
            sum = a[start] + a[end];
            if (sum == x) ans ++;
            if (sum <= x) start++;
            else end--;
        }
        System.out.println(ans);
    }
}
