import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

/**
 * @FileName :
 * @Link : https://www.acmicpc.net/problem/
 * @Date : 2021/02/24
 */
public class Q1065 {
    public static int arithmetic_sequence(int num) {
        int cnt = 0;
        if (num < 100) { // 1~99 의 경우 그 수 자체가 수열
            return num;
        } else {
            cnt = 99;
            if (num == 1000) { // 1000은 등차수열이 아니기 때문에 999로 변경 (예외처리)
                num = 999;
            }

            for (int i = 100; i <= num; i++) {
                int hun = i / 100; // 백의 자릿 수
                int ten = (i / 10) % 10; // 십의 자릿 수
                int one = i % 10;

                if ((hun - ten) == (ten - one)) { // 각 자릿수가 수열을 이루면
                    cnt++;
                }
            }
        }
        return cnt;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println(arithmetic_sequence(Integer.parseInt(br.readLine())));
    }
}
