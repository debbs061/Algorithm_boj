import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Q2750 {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(br.readLine());
        }
        insertionSort(a, n);

        for (int i = 0; i < n; i++) {
            System.out.println(a[i]);
        }
    }
    static void swap(int a[], int idx1, int idx2) {
        int tmp = a[idx1];
        a[idx1] = a[idx2];
        a[idx2] = tmp;

    }
    static void insertionSort(int a[], int n) {
        for (int i = 1; i < n; i++) {
            for (int j = i; j >= 1; j--) {
                if (a[j] < a[j-1])
                    swap(a, j, j-1);
                else
                    break;
            }
        }
    }
}