import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Q5622 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String dial = br.readLine();
        int ans = 0;
        for (int i = 0; i < dial.length(); i++) {
            char a = dial.charAt(i);
            if (a == 'A' || a == 'B' || a == 'C') {
                ans += 3;
            } else if (a == 'D' || a == 'E' || a == 'F') {
                ans += 4;
            } else if (a == 'G' || a == 'H' || a == 'I') {
                ans += 5;
            } else if (a == 'J' || a == 'K' || a == 'L') {
                ans += 6;
            } else if (a == 'M' || a == 'N' || a == 'O') {
                ans += 7;
            } else if (a == 'P' || a == 'Q' || a == 'R' || a == 'S') {
                ans += 8;
            } else if (a == 'T' || a == 'U' || a == 'V') {
                ans += 9;
            } else if (a == 'W' || a == 'X' || a == 'Y' || a == 'Z') {
                ans += 10;
            }
        }
        System.out.println(ans);
    }
}
