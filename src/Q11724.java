import java.util.ArrayList;
import java.util.Scanner;

/**
* @fileName : Q11724.java
* @date : 2021. 2. 2.
* @문제이름 : 연결 요소의 개수
* @문제링크 : https://www.acmicpc.net/problem/11724
*/
public class Q11724 {
	public static void dfs(ArrayList<Integer>[] a, boolean[] c ,int x) {
		if (c[x]) {
			return;
		}
		c[x] = true; 
		for (int y : a[x]) {
			if (c[y] == false) {
				dfs(a, c, y);
			}
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		ArrayList<Integer>[] a = (ArrayList<Integer>[]) new ArrayList[n+1];
		// 정점 개수만큼 인접리스트 추가
		for(int i=1; i<=n; i++) {
			a[i] = new ArrayList<Integer>();
		}
		// 간선 추가
		for(int i=0; i<m; i++) {
			int u = sc.nextInt();
			int v = sc.nextInt();
			a[u].add(v);
			a[v].add(u);
		}
		boolean[] check = new boolean[n+1];
		int ans = 0;
		for (int i=1; i<=n; i++) {
			if (check[i] == false) {
				dfs(a, check, i);
				ans += 1;
			}
		}
		System.out.println(ans);
	}

}