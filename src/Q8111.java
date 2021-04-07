import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

/**
 * @FileName : 0과 1
 * @Link : https://www.acmicpc.net/problem/8111
 * @Date : 2021/03/04
 */
public class Q8111 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            // 문제에 답이 'N의 배수' 란 조건이 있으면 -> 나올 수 있는 수의 개수가 N개로 줄어든다
            int n = sc.nextInt();
            int[] from = new int[n];
            int[] how = new int[n];
            int[] dist = new int[n];    // n으로 나눈 나머지

            for (int i = 0; i < n; i++) {
                from[i] = how[i] = dist[i] = -1;
            }
            Queue<Integer> q = new LinkedList<>();
            // n이 1인 경우를 맨 처음에 큐에 넣어준다. (1도 n으로 나눈 나머지도 알고 있어야 하므로)
            q.add(1 % n);
            dist[1%n] = 0;
            how[1%n] = 1;
            while (!q.isEmpty()) {
                int now = q.remove();
                for (int i = 0; i <= 1; i++) {  // 0하고 1만 붙을 수 있으므로
                    int next = (now*10+i)%n;
                    if (dist[next] == -1) { // 방문한 적 없으면 (아직 만들어준 적 없는 수면)
                        dist[next] = dist[now] + 1;
                        from[next] = now; // 101 -> 1010 이런식으로 붙는거니까
                        how[next] = i;   // 어디에서 만들었는지
                        q.add(next);
                    }
                }
            }

            // 역순으로 출력하기
            if (dist[0] == -1) {    // 나머지가 0인 게 없다면
                System.out.println("BRAK");
            } else {
                StringBuilder ans = new StringBuilder();
                for (int i = 0; i != -1; i = from[i]) {
                    ans.append(Integer.toString(how[i]));
                }
                System.out.println(ans.reverse());
            }
        }
    }
}
