package etc;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Q4 {

//    public void reversePrint(String str) {
//        String reverseStr = "";
//        char[] t = str.toCharArray();
//        for (int i = 0; i < t.length / 2; i++) {
//            char tmp = t[i];
//            t[i] = t[t.length-1-i];
//            t[t.length-1-i] = tmp;
//        }
//        reverseStr = String.copyValueOf(t);
//
//        System.out.println(reverseStr);
//    }

    public void reversePrint(String str) {
        String reverseStr = "";
        StringBuilder s = new StringBuilder(str);
        System.out.println(s.reverse());
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Q4 q = new Q4();
        String s[] = new String[n];

        for (int i = 0; i < n; i++) {
            s[i] = br.readLine();
        }
        for (int i = 0; i < n; i++) {
            q.reversePrint(s[i]);
        }

    }
}
