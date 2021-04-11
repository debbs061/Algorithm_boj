import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Pair9376 {
    int x, y;

    Pair9376(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Q9376 {
    public static final int dx[] = {0, 0, 1, -1};
    public static final int dy[] = {1, -1, 0, 0};

    public static int[][] bfs(String[] a, int x, int y) {
        int n = a.length;
        int m = a[0].length();
        int[][] d = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                d[i][j] = -1;
            }
        }
        ArrayDeque<Pair9376> q = new ArrayDeque<>();
        q.add(new Pair9376(x, y));
        while (!q.isEmpty()) {
            Pair9376 p = q.poll();
            x = p.x;
            y = p.y;
            for (int l = 0; l < 4; l++) {
                int nx = x + dx[l];
                int ny = y + dy[l];
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (d[nx][ny] != -1) continue;
                    char c = a[nx].charAt(ny);
                    if (c == '*') continue;
                    if (c == '#') {
                        d[nx][ny] = d[x][y] + 1;
                        q.addLast(new Pair9376(nx, ny));
                    } else {
                        d[nx][ny] = d[x][y];
                        q.addFirst(new Pair9376(nx, ny));
                    }

                }
            }
        }

        return d;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int t = Integer.parseInt(br.readLine());
        int[] dap = new int[t];
        while (t-- > 0) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            String[] a = new String[n + 2];
            for (int i = 1; i <= n; i++) {
                a[i] = br.readLine();
                a[i] = "." + a[i] + ".";
            }
            n +=2;
            m +=2;
            a[0] = a[n-1] = "";
            for (int j = 0; j < m; j++) {
                a[0] += ".";
                a[n - 1] += ".";
            }

            int[][] d0 = bfs(a, 0, 0);
            int x1, y1, x2, y2;
            x1 = y1 = x2 = y2 = -1;

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (a[i].charAt(j) == '$') {
                        if (x1 == -1) {
                            x1 = i;
                            y1 = j;
                        } else {
                            x2 = i;
                            y2 = j;
                        }
                    }
                }
            }
            int[][] d1 = bfs(a, x1, y1);
            int[][] d2 = bfs(a, x2, y2);

            int ans = n*m;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    char c = a[i].charAt(j);
                    if (c == '*') continue;
                    int cur = d0[i][j] + d1[i][j] + d2[i][j];
                    if (c == '#') cur -= 2;
                    if (ans > cur) ans = cur;
                }
            }
            dap[t] = ans;
        }
        for (int tmp : dap) {
            System.out.println(tmp);
        }
    }
}



