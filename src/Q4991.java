/**
 * @FileName :
 * @Link : https://www.acmicpc.net/problem/
 * @Date : 2021/03/04
 */

import java.util.*;

class Pair4991 {
    int first;
    int second;

    Pair4991(int first, int second) {
        this.first = first;
        this.second = second;
    }
}

public class Q4991 {
    static final int[] dx = {0, 0, 1, -1};
    static final int[] dy = {1, -1, 0, 0};

    static int[][] bfs(String[] a, int sx, int sy) {
        int n = a.length;
        int m = a[0].length();
        int[][] dist = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                dist[i][j] = -1;
            }
        }
        Queue<Pair4991> q = new LinkedList<Pair4991>();
        q.add(new Pair4991(sx, sy));
        dist[sx][sy] = 0;
        while (!q.isEmpty()) {
            Pair4991 p = q.remove();
            int x = p.first;
            int y = p.second;
            for (int k = 0; k < 4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (dist[nx][ny] == -1 && a[nx].charAt(ny) != 'x') {
                        dist[nx][ny] = dist[x][y] + 1;
                        q.add(new Pair4991(nx, ny));
                    }
                }
            }
        }
        return dist;
    }

    static boolean next_permutation(int[] a) {
        int i = a.length - 1;
        while (i > 0 && a[i - 1] >= a[i]) {
            i -= 1;
        }
        if (i <= 0) {
            return false;
        }
        int j = a.length - 1;
        while (a[j] <= a[i - 1]) {
            j -= 1;
        }
        int temp = a[i - 1];
        a[i - 1] = a[j];
        a[j] = temp;
        j = a.length - 1;
        while (i < j) {
            temp = a[i];
            a[i] = a[j];
            a[j] = temp;
            i += 1;
            j -= 1;
        }
        return true;
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            int m = sc.nextInt();
            int n = sc.nextInt();
            if (n == 0 && m == 0) break;
            String[] a = new String[n];
            for (int i = 0; i < n; i++) {
                a[i] = sc.next();
            }
            ArrayList<Pair4991> b = new ArrayList<>();
            b.add(new Pair4991(0, 0));
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    char x = a[i].charAt(j);
                    if (x == 'o') { // 출발지
                        b.set(0, new Pair4991(i, j));
                    } else if (x == '*') {  // 더러운 방
                        b.add(new Pair4991(i, j));
                    }
                }
            }
            int l = b.size();
            int[][] d = new int[l][l];
            boolean ok = true;
            for (int i = 0; i < l; i++) {
                int[][] dist = bfs(a, b.get(i).first, b.get(i).second);
                for (int j = 0; j < l; j++) {
                    d[i][j] = dist[b.get(j).first][b.get(j).second];
                    if (d[i][j] == -1) {
                        ok = false;
                    }
                }
            }
            if (ok == false) {
                System.out.println(-1);
                continue;
            }
            int[] p = new int[l - 1];
            for (int i = 0; i < l - 1; i++) {
                p[i] = i + 1;
            }
            int ans = -1;
            do {
                int now = d[0][p[0]];
                for (int i = 0; i < l - 2; i++) {
                    now += d[p[i]][p[i + 1]];
                }
                if (ans == -1 || ans > now) {
                    ans = now;
                }
            } while (next_permutation(p));
            System.out.println(ans);
        }
    }
}

