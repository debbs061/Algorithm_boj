import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 * @FileName : 1987
 * @Link : https://www.acmicpc.net/problem/1987
 * @Date : 2021/02/26
 */

class Pair1987 {
    int x, y;

    Pair1987(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Q1987 {
    public static final int dx[] = {0, 0, 1, -1};
    public static final int dy[] = {1, -1, 0, 0};
    public static int r;
    public static int c;
    public static int go(char[][] a, boolean[] check, int x, int y) {
        int ans = 0;
        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];
            if (nx >= 0 && nx < c && ny >= 0 && ny < r) {
                if (!check[a[nx][ny] - 'A']) {
                    check[a[nx][ny] - 'A'] = true;
                    int next = go(a, check, nx, ny);
                    if (ans < next) {
                        ans = next;
                    }
                    check[a[nx][ny] - 'A'] = false;
                }
            }
        }
        return ans + 1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        c = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        char a[][] = new char[c][r];

        for (int i = 0; i < c; i++) {
            String tmp = br.readLine();
            for (int j = 0; j < r; j++) {
                a[i][j] = tmp.charAt(j);
            }
        }
        boolean[] check = new boolean[26];
        check[a[0][0] - 'A'] = true;
        System.out.println(go(a, check, 0, 0));


    }
}
