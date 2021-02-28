import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 * @FileName : 숨바꼭질
 * @Link : https://www.acmicpc.net/problem/1697
 * @Date : 2021. 1. 29. 
 */
public class Q1697 {
	public static final int MAX = 1000000;
	
	public static void main(String[] args) throws IOException {
		InputStream in = System.in;
		BufferedReader br = new BufferedReader(new InputStreamReader(in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		boolean[] check = new boolean[MAX];
		int[] dist = new int[MAX];			// i를 몇 번만에 방문했는지
		check[n] = true;
		dist[n] = 0;
			
		Queue<Integer> q = new LinkedList<Integer>();
		q.add(n);

		// now -> next로 가는 가장 빠른 거리
		while(!q.isEmpty()) {
			int now = q.remove();
			if (now-1 >= 0) {
				if (!check[now - 1]) {
					q.add(now-1);			// 방문한 적 없으면 무조건 방문해야함. 그래야 최단거리를 구할 수 있음.
					check[now-1] = true;
					dist[now-1] = dist[now] + 1;
				}
			}
			
			if (now+1 < MAX) {
				if (!check[now + 1]) {
					q.add(now+1);
					check[now+1] = true;
					dist[now+1] = dist[now] + 1;
				}
			}
			
			if (now*2 < MAX) {
				if (check[now*2] == false) {
					q.add(now*2);
					check[now*2] = true;
					dist[now*2] = dist[now] + 1;
				}
			}
		}
		System.out.println(dist[k]);
	}

}
