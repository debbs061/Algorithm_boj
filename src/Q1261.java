import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Pair1261 {
    int x, y;

    Pair1261(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

/**
 * @FileName : 알고스팟
 * @Link : https://www.acmicpc.net/problem/1261
 * @Date : 2021. 1. 29.
 */
public class Q1261 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();
        sc.nextLine();
        int[][] a = new int[n][m];
        for (int i = 0; i < n; i++) {
            String s = sc.nextLine();
            for (int j = 0; j < m; j++) {
                a[i][j] = s.charAt(j) - '0';
            }
        }
        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};
        int[][] d = new int [n][m];
        Queue<Pair1261> q = new LinkedList<Pair1261>();
        Queue<Pair1261> next_queue = new LinkedList<Pair1261>();
        q.offer(new Pair1261(0, 0));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                d[i][j] = -1;
            }
        }
        d[0][0] = 0;
        while (!q.isEmpty()) {
            Pair1261 p = q.remove();
            int x= p.x;
            int y = p.y;
            for (int k = 0; k < 4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (d[nx][ny] == -1) {
                        if (a[nx][ny] == 0) {
                            d[nx][ny] = d[x][y];
                            q.offer(new Pair1261(nx, ny));
                        } else {
                            d[nx][ny] = d[x][y] + 1;
                            next_queue.offer(new Pair1261(nx, ny));
                        }
                    }
                }
            }
            if (q.isEmpty()) {
                q = next_queue;
                next_queue = new LinkedList<Pair1261>();
            }
        }
        System.out.println(d[n-1][m-1]);
    }
}
