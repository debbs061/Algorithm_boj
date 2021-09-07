package etc;

import java.util.Scanner;

/**
 * 문장 속 단어
 */
public class Q3 {

    public String solution(String str) {
        String answer = "";
        int m = Integer.MIN_VALUE, pos;
        while ((pos = str.indexOf(' ')) != -1) {
            String tmp = str.substring(0, pos);
            int len = tmp.length();
            if (len > m) {
                m = len;
                answer = tmp;
            }
            str = str.substring(pos+1);
        }
        if (str.length() > m) answer = str;
        return answer;
    }

    public static void main(String[] args){
        Q3 t = new Q3();
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        System.out.println(t.solution(str));
    }
}