import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Q5430 {

    public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        StringTokenizer st;
        Deque<Integer> q;

        while (t-- > 0) {
            String order = br.readLine();
            int n = Integer.parseInt(br.readLine());

            st = new StringTokenizer(br.readLine(), "[],");
            q = new LinkedList<>();

            // 덱에 배열 원소를 넣어준다.
            for (int i = 0; i < n; i++) {
                q.offer(Integer.parseInt(st.nextToken()));
            }

            AC(order, q);
        }

        System.out.println(sb);
    }

    public static void AC(String order, Deque<Integer> q) {

        boolean state = true; // t : 정상 , f : 뒤집어진 상태

        for (int k = 0; k < order.length(); k++) {
            char ord = order.charAt(k);

            if (ord == 'R') {
                state = !state;
                continue;
            }

            // 아래는 D 의 경우
            if (state) {
                if (q.pollFirst() == null) {
                    sb.append("error\n");
                    return;
                }
            } else {
                if (q.pollLast() == null) {
                    sb.append("error\n");
                    return;
                }
            }
        }

        // 모든 함수들이 정상적으로 작동했다면 덱의 남은 요소들을 출력문으로 만들어준다.
        makePrintString(q, state);

    }

    public static void makePrintString(Deque<Integer> q, boolean state) {

        sb.append("[");

        if (q.size() > 0) {     // 만약 출력 할 원소가 한 개 이상일 경우

            if (state) {

                sb.append(q.pollFirst());

                while (!q.isEmpty()) {
                    sb.append(',').append(q.pollFirst());
                }

            } else {

                sb.append(q.pollLast());

                while (!q.isEmpty()) {
                    sb.append(',').append(q.pollLast());
                }

            }
        }

        sb.append("]\n");

    }

}
