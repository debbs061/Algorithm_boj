package etc;

import com.sun.tools.javac.Main;

import java.util.Locale;
import java.util.Scanner;

/**
 * 1. 문자 찾기
 */
public class Q1 {

    public int solution(String str, char t) {
        int answer = 0;
        str = str.toUpperCase();
        t = Character.toUpperCase(t);
        for (char x : str.toCharArray()) {
            if (x == t) answer ++;
        }
        return answer;
    }

    public static void main(String[] args) {
        Q1 q1 = new Q1();
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        char c = sc.next().charAt(0);
        System.out.print(q1.solution(str,c));
    }
}
