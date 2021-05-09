import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Q2630 {

    public static int white = 0;
    public static int blue = 0;
    public static int[][] board;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        board = new int[n][n];

        StringTokenizer st;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        partition(0, 0, n);

        System.out.println(white);
        System.out.println(blue);

    }

    public static void partition(int row, int col, int size) {
        if (colorCheck(row, col, size)) {
            if (board[row][col] == 0) {
                white ++;
            } else {
                blue ++;
            }
            return;
        }

        int newSize = size / 2;
        // 재귀 호출
        partition(row, col, newSize);
        partition(row, col + newSize, newSize);
        partition(row + newSize, col, newSize);
        partition(row + newSize, col + newSize, newSize);
    }

    // 현재 파티션의 컬러가 같은지 체크
    public static boolean colorCheck(int row, int col, int size) {
        int color = board[row][col]; // 첫 번째 원소를 기준으로 검사
        for (int i = row; i < row + size; i++) {
            for (int j = col; j < col + size; j++) {
                // 색상이 같지 않다면 false 리턴
                if (board[i][j] != color) {
                    return false;
                }
            }
        }
        return true;
    }

}
