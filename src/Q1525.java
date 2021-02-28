import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

/**
 * @FileName : 퍼즐
 * @Link : https://www.acmicpc.net/problem/1525
 * @Date : 2021. 2. 28.
 */
public class Q1525 {
	public static final int[] dx = {0, 0, 1, -1};
	public static final int[] dy = {1, -1, 0, 0};
	
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int n = 3;
		int start = 0;
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				int temp = sc.nextInt();
				if (temp == 0) {		// 빈칸이 나오면 9로 치환
					temp = 9;
				}
				start = start * 10 + temp;	// 9자리 정수로 만들어주는 과정
			}
		}

		Queue<Integer> q = new LinkedList<Integer>();
		HashMap<Integer,Integer> d  = new HashMap<Integer,Integer>();	// 예를들어 123456789 까지 걸리는 최단거리가 저장됨
		d.put(start, 0);
		q.add(start);
		while (!q.isEmpty()) {
			int now_num = q.remove();	// 정수를 담음 
			String now = Integer.toString(now_num); //문자열로 바꿔서 담음 
			int z = now.indexOf('9'); // 공백의 위치 (x,y) 
			int x = z/3;
			int y = z%3;
			
			for(int k=0; k<4; k++) {
				int nx = x+dx[k];
				int ny = y+dy[k];
				if (nx >= 0 && nx < n && ny >= 0 && ny < n) { // 다음 칸이 3x3 범위를 벗어나지 않는다면 
					StringBuilder next = new StringBuilder(now);
					char temp = next.charAt(x*3+y);
					next.setCharAt(x*3+y, next.charAt(nx*3+ny));
					next.setCharAt(nx*3+ny, temp);
					int num = Integer.parseInt(next.toString());
					if (!d.containsKey(num)) {
						d.put(num, d.get(now_num)+1);	// 123456789 까지 가는데 걸리는 최단거리
						q.add(num);
					}
				}
			}
		}
		if (d.containsKey(123456789)) {
			System.out.println(d.get(123456789));
		} else {
			System.out.println("-1");
		}
	}
	
	
	
}
