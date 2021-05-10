import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Q2447 {
    static char[][] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        arr = new char[n][n];

        star(0, 0, n, false);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                sb.append(arr[i][j]);
            }
            sb.append('\n');
        }
        System.out.print(sb);
    }

    static void star(int x, int y, int n, boolean blank) {
        // 공백칸일 경우
        if (blank) {
            for (int i = x; i < x + n; i++) {
                for (int j = y; j < y + n; j++) {
                    arr[i][j] = ' ';
                }
            }
            return;
        }

        // 더이상 쪼갤 수 없는 블록일 때
        if (n == 1) {
            arr[x][y] = '*';
            return;
        }

        /*
            N = 27 일 경우 한 블록의 사이즈는 9이고,
            N = 9 일 경우 한 블록의 사이즈는 3이듯
            해당 블록의 한 칸을 담을 변수를 의미
         */
        int size = n/3;
        int count = 0;
        for (int i = x; i < x + n; i += size) {
            for (int j = y; j < y + n; j += size) {
                count ++;
                if (count == 5) {
                    star(i, j, size, true);
                } else {
                    star(i, j, size, false);
                }
            }
        }
    }
}
