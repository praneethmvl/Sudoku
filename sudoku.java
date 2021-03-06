package praaject;

class sudoku {
	int k[][] = new int[9][9];
	int backtracks = 0;

	public sudoku() {
		k = new int[][] { { 3, 0, 6, 5, 0, 8, 4, 0, 0 }, { 5, 2, 0, 0, 0, 0, 0, 0, 0 }, { 0, 8, 7, 0, 0, 0, 0, 3, 1 },
				{ 0, 0, 3, 0, 1, 0, 0, 8, 0 }, { 9, 0, 0, 8, 6, 3, 0, 0, 5 }, { 0, 5, 0, 0, 9, 0, 6, 0, 0 },
				{ 1, 3, 0, 0, 0, 0, 2, 5, 0 }, { 0, 0, 0, 0, 0, 0, 0, 7, 4 }, { 0, 0, 5, 2, 0, 6, 3, 0, 0 } };
	}

	public static void main(String args[]) {
		int p[][] = new int[9][9];
		// boolean ans;
		sudoku obj = new sudoku();
		p = obj.k;
		// ans = obj.check(5, 5, 1);
		// System.out.println(ans);
		obj.printMat();
		obj.solve();
		System.out.println("########################################");
		obj.printMat();

		System.out.print(obj.backtracks);

	}

	public boolean check(int x, int y, int num) {

		for (int i = 0; i < 9; i++) {
			if (k[x][i] == num) // column
				return false;
		}
		for (int i = 0; i < 9; i++) {
			if (k[i][y] == num) // row
				return false;
		}
		int qx = quad(x);
		int qy = quad(y);
		for (int i = qx; i < qx + 3; i++) {
			for (int j = qy; j < qy + 3; j++) {
				if (k[i][j] == num)
					return false;
			}
		}
		return true;
	}

	public int quad(int loc) {
		int q = 0;
		if (loc >= 0 && loc <= 2) {
			q = 0;
		}
		if (loc >= 3 && loc <= 5) {
			q = 3;
		}
		if (loc >= 6 && loc <= 8) {
			q = 6;
		}
		return q;
	}

	public void printMat() {
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				System.out.print(k[i][j] + " ");
			}
			System.out.println();
		}
	}

	public boolean solve() {
		for (int i = 0; i < 9; i++) {
			for (int j = 0; j < 9; j++) {
				// System.out.println("Inside Rec " + i + " " + j);
				if (k[i][j] == 0) {
					// System.out.println("Inside Rec" + i + " " + j);
					for (int n = 1; n <= 9; n++) {
						if (check(i, j, n) == true) {
							k[i][j] = n;
							if (solve() == true) {
								return true;
							} else {
								k[i][j] = 0;
								backtracks++;
							}
						}
					}
					return false;
				}

			}
		}
		return true;
	}
}
