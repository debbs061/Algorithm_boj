import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Q10845 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        Deque<Integer> q = new LinkedList<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String order = st.nextToken();
            if (order.equals("push")) {
                q.offer(Integer.parseInt(st.nextToken()));
            } else if (order.equals("pop")) {
                Integer tmp = q.poll();
                if (tmp != null) {
                    sb.append(tmp).append('\n');
                } else {
                    sb.append(-1).append('\n');
                }
            } else if (order.equals("size")) {
                sb.append(q.size()).append('\n');
            } else if (order.equals("empty")) {
                if (q.isEmpty()) {
                    sb.append(1).append('\n');
                } else {
                    sb.append(0).append('\n');
                }
            } else if (order.equals("front")) {
                Integer tmp = q.peek();
                if (tmp != null) {
                    sb.append(tmp).append('\n');
                } else {
                    sb.append(-1).append('\n');
                }
            } else if (order.equals("back")) {
                Integer tmp = q.peekLast();
                if (tmp != null) {
                    sb.append(tmp).append('\n');
                } else {
                    sb.append(-1).append('\n');
                }
            }
        }
        System.out.println(sb);
    }
}
