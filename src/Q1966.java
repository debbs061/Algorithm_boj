import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Q1966 {
    static int solution(int[] priorities, int location) {
        int answer = 0;
        int index = 0;
        int max_change = 0;

        ArrayList<Integer> prior = new ArrayList<>();    // 단순히 max값을 알기 위한 용도

        for (int i = 0; i < priorities.length; i++) {
            prior.add(priorities[i]);
        }

        Collections.sort(prior);
        Collections.reverse(prior);
        int max = prior.get(0);

        while (true) {
            // 출력부
            if (priorities[index] == max) {
                priorities[index] = -1;
                answer++;
                max_change = 1; // 출력했으면 방금 그 출력물이 target인지 아래서 확인하기 위한 용도
            }
            // 출력 x -> index 만 바꿔주면 됨.
            // index가 끝까지 갔으면 다시 0부터 확인하면 됨 (계속 원본 배열안에서는 반복)
            else {
                if (index == priorities.length - 1) {
                    index = 0;
                } else {
                    index ++;
                }
            }

            /**
             *   아래는 출력한 경우에 일어나는 로직들
             */

            // 방금 출력한 게 내가 원하는 문서였다면, brea
            if (priorities[location] == -1) {
                break;
            }

            // 아니라면, 기존의 max값은 출력된 상태이니깐 max값이 바껴야함
            if (max_change == 1) {
                prior.remove(0);
                max = prior.get(0);
                max_change = 0;
            }

        }
        return answer;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int t = Integer.parseInt(br.readLine());
        int number[] = new int[t];
        for (int i = 0; i < t; i++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken()); // 문서 개수
            int k = Integer.parseInt(st.nextToken()); // 궁금한 문서 인덱스 위치
            int a[] = new int[n]; // 중요도
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                a[j] = Integer.parseInt(st.nextToken());
            }
            number[i] = solution(a,  k);
        }

        for (int i = 0; i < t; i++) {
            System.out.println(number[i]);
        }
    }
}
