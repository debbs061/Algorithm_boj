import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;


public class Q1012 {

    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static final int[] dx = {0, 0, 1, -1};
    static final int[] dy = {1, -1, 0, 0};

    static int n;
    static int m;
    static int k;

    // 배추맵 (true: 심어져있는 경우)
    static boolean a[][];

    // 배추 방문 여부
    static boolean check[][];

    static void dfs(int x, int y) {
        check[x][y] = true;
        for (int j = 0; j < 4; j++) {
            int nx = x + dx[j];
            int ny = y + dy[j];

            // 갈 공간이 있으면
            if (0 <= nx && nx < m && 0 <= ny && ny < n) {
                if (check[nx][ny] || !a[nx][ny]) {
                    continue;
                }
                dfs(nx, ny);
            }
        }
    }

    public static void main(String args[]) throws NumberFormatException, IOException {

        int t = Integer.parseInt(br.readLine());
        int ans;

        for (int p = 0; p < t; p++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            m = Integer.parseInt(st.nextToken());
            n = Integer.parseInt(st.nextToken());
            k = Integer.parseInt(st.nextToken());

            a = new boolean[m][n];
            check = new boolean[m][n];
            ans = 0;

            // 배추 심은곳 true로 바꿔주기
            for (int l = 0; l < k; l++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                a[x][y] = true;
            }


            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (!check[i][j] && a[i][j] == true) {
                        dfs(i, j);
                        ans++;
                    }
                }
            }
            sb.append(ans + "\n");
        }
        System.out.println(sb);
    }
}