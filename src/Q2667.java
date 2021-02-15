import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

/**
 * @FileName : 단지번호 붙이기
 * @Link : https://www.acmicpc.net/problem/2667
 * @Date : 2021. 2. 2.
 */
class Pair2667 {
	int x;
	int y;
	Pair2667(int x, int y) {
		this.x = x;
		this.y = y;
	}
}

public class Q2667 {
	public static final int[] dx = {0, 0, 1, -1};
	public static final int[] dy = {1, -1, 0, 0};
	
	public static void bfs(int[][] a, int[][] group, int x, int y, int cnt, int n) {
		Queue<Pair2667> q = new LinkedList<Pair2667>();
		q.add(new Pair2667(x, y)); 
		group[x][y] = cnt;
		while (!q.isEmpty()) {
			Pair2667 p = q.remove();
			x = p.x;
			y = p.y;
			for (int k=0; k<4; k++) {
				int nx = x+dx[k];
				int ny = y+dy[k];
				if (0 <= nx && nx < n && 0 <= ny && ny < n) {
					if (a[nx][ny] == 1 && group[nx][ny] == 0) {
						q.add(new Pair2667(nx, ny));
						group[nx][ny] = cnt;
					}
				}	
			}
			
		}
	}

	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int [][] a = new int[n][n];
		for(int i=0; i<n; i++) {
			String str = br.readLine();
			for(int j=0; j<n; j++) {
				a[i][j] = str.charAt(j) - '0';
			}
		}
		
		int cnt = 0;
		int[][] group = new int[n][n]; // 단지 번호 
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				if (a[i][j] == 1 && group[i][j] == 0) {
					bfs(a, group, i, j, ++cnt, n);
				}
			}
		}
		
		int[] ans = new int[cnt];
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				if (group[i][j] != 0) {
					ans[group[i][j]-1] += 1;
				}
			}
		}
		Arrays.sort(ans);
		System.out.println(cnt);
		for (int i=0; i<cnt; i++) {
			System.out.println(ans[i]);
		}
	}
}
