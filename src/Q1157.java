import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

/**
 * @FileName : Q1157
 * @Link : https://www.acmicpc.net/problem/1157
 * @Date : 2021/02/24
 */
public class Q1157 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] arr = new int[26]; // 영문자의 개수는 26개
        String s = br.readLine();

        for (int i = 0; i < s.length(); i++) {
            if ('a' <= s.charAt(i) && s.charAt(i) <= 'z') { // 소문자범위
                arr[s.charAt(i) - 'a']++;
            } else {                                        // 대문자범위
                arr[s.charAt(i) - 'A']++;
            }
        }

        int max = -1;
        char ch = '?';

        for (int i = 0; i < 26; i++) {
            if (arr[i] > max) {
                max = arr[i];
                ch = (char) (i + 65); // 대문자로 출력해야 하므로 65를 더해준다
            } else if (arr[i] == max){
                ch = '?';
            }
        }
        System.out.println(ch);
    }
}
