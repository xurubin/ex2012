import java.util.Scanner;

public class ex2012 {
    public static void main(String[] argu) {
		int[][] data = load();
		int n = data.length;
		int m = data[0].length;
		System.out.println(solve(n, m, data));
	}
	
	private static int[][] load() {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();	
		int m = in.nextInt();
		int[][] result = new int[n][];
		for(int i=0; i<n; i++) {
		    result[i] = new int[m];
			for(int j=0; j<m; j++) 
				result[i][j] = in.nextInt();
		}
		return result;
	}
	private static int solve_test(int n, int m, int[][] data) {
		int result = 0;
		for(int i=0; i<n; i++)
		    for(int j=0; j<m; j++)
				result += data[i][j];
		return result;
	}
	private static int solve(int n, int m, int[][] data) {
	}
}