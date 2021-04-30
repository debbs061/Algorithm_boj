import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class rePair {
    int x;
    int y;
    rePair(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Q7576_re {

    static final int dx[] = {1, -1, 0, 0};
    static final int dy[] = {0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int a[][] = new int[n][m];
        int dist[][] = new int[n][m];
        Queue<rePair> q = new LinkedList<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                a[i][j] = Integer.parseInt(st.nextToken());
                dist[i][j] = -1;
                if (a[i][j] == 1) {
                    q.add(new rePair(i, j));
                    dist[i][j] = 0;
                }
            }
        }

        while (!q.isEmpty()) {
            rePair p = q.poll();
            int x = p.x;
            int y = p.y;
            for (int k = 0; k < 4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (a[nx][ny] == 0 && dist[nx][ny] == -1) {
                        q.add(new rePair(nx, ny));
                        dist[nx][ny] = dist[x][y] + 1;
                    }
                }
            }
        }

        int ans = 0; // 최소 일수
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (ans < dist[i][j]) {
                    ans = dist[i][j];
                }
            }
        }

        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {

                // 토마토가 익지 않았고 간 적도 없으면 -1 반환 (토마토가 전부 익을 수 없는 상황이면 -1 반환하라고 문제에 주워짐)
                if (a[i][j] == 0 && dist[i][j] == -1) {
                    ans = -1;
                }
            }
        }

        System.out.println(ans);

    }


}