import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Q18258 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        Deque<Integer> q = new LinkedList<>();


        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String order = st.nextToken();
            if (order.equals("push")) {
                q.offer(Integer.parseInt(st.nextToken()));
            } else if (order.equals("pop")) {
                /**
                 * poll 은 가장 앞에 있는 요소를 삭제하며
                 * 삭제할 원소가 없을 경우 예외를 던지는 것이 아닌 null 을 반환
                 */
                Integer item = q.poll();
                if (item == null) {
                    sb.append(-1).append('\n');
                } else {
                    sb.append(item).append('\n');
                }
            } else if (order.equals("size")) {
                sb.append(q.size()).append('\n');
            } else if (order.equals("empty")) {
                if (q.isEmpty()) {
                    sb.append(1).append('\n');
                } else
                    sb.append(0).append('\n');
            } else if (order.equals("front")) {
                /**
                 * peek() 은 큐에 꺼낼 요소가 없을 경우 null 을 반환
                 */
                Integer ite = q.peek();
                if (ite == null) {
                    sb.append(-1).append('\n');
                } else {
                    sb.append(ite).append('\n');
                }
            } else {
                /**
                 * peekLast() 는 큐에 꺼낼 요소가 없을 경우 null 을 반환
                 */
                Integer it = q.peekLast();
                if (it == null) {
                    sb.append(-1).append('\n');
                } else {
                    sb.append(it).append('\n');
                }
            }
        }
        System.out.println(sb);
    }
}
