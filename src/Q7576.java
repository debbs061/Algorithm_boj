import java.util.*;

class Pair7576 {
	int x;
	int y;
	Pair7576(int x, int y) {
		this.x = x;
		this.y = y;
	}
}

/**
 * @FileName : 토마토
 * @Link : https://www.acmicpc.net/problem/7576
 * @Date : 2021. 2. 2.
 */
public class Q7576 {
    public static final int[] dx = {0, 0, 1, -1};
    public static final int[] dy = {1, -1, 0, 0};
    
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);	// BufferedReader
        int m = sc.nextInt();
        int n = sc.nextInt();
        int[][] a = new int[n][m];		// 익었는지 안 익었는지 
        int[][] dist = new int[n][m];	// 칸(i,j) 별로 며칠 후에 익는지 일수를 담음
        Queue<Pair7576> q = new LinkedList<Pair7576>();
        
        // 입력받음
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                a[i][j] = sc.nextInt();
                dist[i][j] = -1;
                
                // 익은 경우
                if (a[i][j] == 1) {
                    q.add(new Pair7576(i, j));
                    dist[i][j] = 0;
                }
                
            }
        }
        while (!q.isEmpty()) {
            Pair7576 p = q.remove();
            int x = p.x;
            int y = p.y;
            for (int k=0; k<4; k++) {
                int nx = x+dx[k];
                int ny = y+dy[k];
                
                // 갈 공간이 있으면
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                	
                	// 토마토 안 익었고, 간 적 없는 곳이면
                    if (a[nx][ny] == 0 && dist[nx][ny] == -1) {
                        q.add(new Pair7576(nx, ny));
                        dist[nx][ny] = dist[x][y] + 1;	// 하루 일수 추가
                    }
                }
                
            }
        }
        
        // Math
        int ans = 0;	// 최소 일수
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                if (ans < dist[i][j]) {
                    ans = dist[i][j];
                }
            }
        }
        
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
            	
            	// 토마토가 익지 않았고 간 적도 없으면 -1 반환 (토마토가 전부 익을 수 없는 상황이면 -1 반환하라고 문제에 주워짐)
                if (a[i][j] == 0 && dist[i][j] == -1) { 
                    ans = -1;
                }
            }
        }
        System.out.println(ans);
        // StringBuilder
    }
}