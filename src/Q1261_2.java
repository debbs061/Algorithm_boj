import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class PairQ1261_2{
    int x, y;
    PairQ1261_2 (int x, int y) {
        this.x = x;
        this.y = y;
    }
}

/**
 * @FileName : 알고스팟
 * @Link : https://www.acmicpc.net/problem/1261
 * @Date : 2021. 2. 17.
 */
public class Q1261_2 {
    public static final int[] dx = {0, 0, 1, -1};
    public static final int[] dy = {1, -1, 0, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int a[][] = new int[n][m];
        int d[][] = new int[n][m];  // 벽을 부수는 횟수

        boolean check[][] = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            String tmp = br.readLine();
            for (int j = 0; j < m; j++) {
                a[i][j] = tmp.charAt(j) - '0';
            }
        }

        ArrayDeque<PairQ1261_2> deque = new ArrayDeque<>();
        deque.add(new PairQ1261_2(0, 0));

        // 방문했는지 여부를 저장함과 동시에, 벽을 부수는 횟수 저장 (방문 안했으면 -1)
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                d[i][j] = -1;
            }
        }

        d[0][0] = 0;
        while (!deque.isEmpty()) {
            PairQ1261_2 p = deque.poll(); // 가장 먼저 보관한 값을 뺴냄
            int x = p.x;
            int y = p.y;
            for (int k = 0; k < 4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];

                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (d[nx][ny] == -1) {
                        if (a[nx][ny] == 0) {   // 벽 안 부수는 경우
                            d[nx][ny] = d[x][y];
                            deque.addFirst(new PairQ1261_2(nx, ny));
                        } else {    // 벽 부수는 경우
                            d[nx][ny] = d[x][y] + 1;
                            deque.addLast(new PairQ1261_2(nx,ny));
                        }

                    }
                }
            }
        }
        System.out.println(d[n-1][m-1]);
    }
}
