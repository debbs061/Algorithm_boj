import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 * @FileName : Q1303
 * @Link : https://www.acmicpc.net/problem/1303
 * @Date : 2021/02/19
 */
class Pair1303 {
	int x;
	int y;
	Pair1303(int x, int y) {
		this.x = x;
		this.y = y;
	}
}

public class Q1303 {
	public static final int[] dx = {0, 0, 1, -1};
	public static final int[] dy = {1, -1, 0, 0};
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int m = Integer.parseInt(st.nextToken()); // 가로
		int n = Integer.parseInt(st.nextToken()); // 세로  

		char [][] map = new char[n][m];
		
		for (int i=0; i<n; i++) {
			String s = br.readLine();
			for (int j=0; j<m; j++) {
				map[i][j] = s.charAt(j);
			}
		}
		
		Queue<Pair1303> q= new LinkedList<Pair1303>();
		
		int white = 0, blue = 0;
		
		for (int i=0; i<n; i++) {
			for (int j=0; j<m; j++) {
				if (map[i][j]!='V') {	// 방문했으면 V로 치환
					char team = map[i][j];
					int count = 1;
					q.add(new Pair1303(i, j));
					map[i][j] = 'V';
					
					while (!q.isEmpty()) {
						Pair1303 p = q.remove();
						int x = p.x;
						int y = p.y;
						for (int k=0; k<4; k++) {
							int nx = x+dx[k];
							int ny = y+dy[k];
							if (0 <= nx && nx <n && 0 <= ny && ny < m) {
								if (map[nx][ny] == team) {
									map[nx][ny] = 'V';
									count ++;
									q.add(new Pair1303(nx, ny));
								}
							}
						}
					}
					
					if (team == 'W') white += count*count;
					else blue += count*count;
					
				}
			}
		}
		System.out.println(white + " " + blue);
		
	}

}
