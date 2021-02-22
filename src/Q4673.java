/**
 * @FileName :
 * @Link : https://www.acmicpc.net/problem/
 * @Date : 2021/02/23
 */

public class Q4673 {

    public static void main(String args[]) {
        boolean check[] = new boolean[10001];
        for (int i = 1; i < 10001; i++) {
            String tmp = Integer.toString(i);
            int result = i;
            for (int j = 0; j < tmp.length(); j++) {
                result += tmp.charAt(j) - '0';
            }
            if (result > 10000) continue;
            check[result] = true;
        }

        for (int i = 1; i < 10001; i++) {
            if (!check[i]) {
                System.out.println(i);
            }
        }

    }
}
