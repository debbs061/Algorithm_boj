import java.util.*;

class Pair2178 {
	int x;
	int y;
	Pair2178(int x, int y) {
		this.x = x;
		this.y = y;
	}
}


public class Q2178 {
    public static final int[] dx = {0, 0, 1, -1};
    public static final int[] dy = {1, -1, 0, 0};
    
    /*
     * Q 2178. 미로탐색 
     * 1: 이동할 수 있는 칸, 0: 이동할 수 없는 칸
     * (1,1) -> (N,M) 이동 최소 칸 수 구하는 문제 
     */
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] a = new int[n][m];
        sc.nextLine();
        
        // 입력받음
        for (int i=0; i<n; i++) {
            String s = sc.nextLine();
            for (int j=0; j<m; j++) {
                a[i][j] = s.charAt(j) - '0';	// int로 변환
            }
        }
        
        int[][] dist = new int[n][m];			
        boolean[][] check = new boolean[n][m];	// 방문 했는지 안했는지
        Queue<Pair2178> q = new LinkedList<Pair2178>();
        q.add(new Pair2178(0, 0));	// (0,0) 부 시작하니깐 큐에 넣음
        check[0][0] = true;
        dist[0][0] = 1;			// 시작점도 이동 수에 포함한다 함
        
        while (!q.isEmpty()) {
            Pair2178 p = q.remove();
            int x = p.x;
            int y = p.y;

        	// 상하좌우 칸 반복문으로 돌기
            for (int k=0; k<4; k++) {
            	
                int nx = x+dx[k];
                int ny = y+dy[k];
                
                // 갈 공간이 있으면
                if (0 <= nx && nx < n && 0 <= ny && ny < m) {
                    if (check[nx][ny] == false && a[nx][ny] == 1) {		// 방문한 적 없고 이동할 수 있는 길이면,
                        q.add(new Pair2178(nx, ny));
                        dist[nx][ny] = dist[x][y] + 1;	// 이동한 칸에 이동 수 + 시켜줌
                        check[nx][ny] = true;
                    }
                }
                
            }
        }
        
        System.out.println(dist[n-1][m-1]);
    }
}