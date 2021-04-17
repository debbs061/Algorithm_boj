import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Q1316 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        int count = 0;

        for (int i = 0; i < n; i++) {
            if (check() == true) {
                count++;
            }
        }
        System.out.println(count);
    }

    // 그룹 단어를 체크하는 함수
    public static boolean check() throws IOException {
        boolean[] check = new boolean[26]; // 영문자 26개
        int prev = 0;
        String str = br.readLine();
        for (int i = 0; i < str.length(); i++) {
            int now = str.charAt(i); // i번째 문자 저장
            if (prev != now) {
                if (check[now - 'a'] == false) {
                    check[now - 'a'] = true;
                    prev = now;
                }
                else {
                    return false;
                }
            }
            // 앞선 문자와 i 번째 문자가 같다면? (연속된 문자)
            else {
                continue;
            }
        }
        return true;
    }
}
