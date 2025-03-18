import java.io.*;
import java.util.*;
import java.math.*;

public class Main {

    public static void main(String[] args) {
        new Main().run();
    }

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    PrintWriter out = new PrintWriter(System.out);
    StringTokenizer st;

    String nextToken() {
        while (st == null || !st.hasMoreTokens()) {
            try {
                st = new StringTokenizer(br.readLine());
            } catch (Exception e) {
                return "0";
            }
        }
        return st.nextToken();
    }

    int nextInt() {
        return Integer.parseInt(nextToken());
    }

    int inBounds(int x, int l, int r, String name) {
        if (x < l || x > r) {
            throw new IllegalArgumentException(name + " is not in bounds: " + x + " is not in [" + l + ".." + r + "]");
        }
        return x;
    }

    private void solve() throws IOException {
        StringBuilder digits = new StringBuilder();
        for (int i = 0; i < 10; i++) {
            digits.append(i);
        }
        for (char c = 'a'; c <= 'z'; c++) {
            digits.append(c);
        }

        int num = inBounds(nextInt(), 1, 1000000000, "num") - 1;
        int l = inBounds(nextInt(), 3, 36, "l");
        int k = inBounds(nextInt(), 2, l - 1, "k");

        int n = 30;
        long[][] a = new long[n + 1][l];
        long sum = 0;
        long pow = 1;

        for (int i = 1; i <= n; i++) {
            long nsum = 0;
            for (int j = 0; j < l; j++) {
                if (j < k) {
                    a[i][j] = sum;
                } else {
                    a[i][j] = pow;
                }
                nsum += a[i][j];
            }
            sum = nsum;
            pow *= l;
            if (sum > num) {
                n = i;
                break;
            }
        }

        StringBuilder sb = new StringBuilder();
        boolean allZero = true;

        outer: for (int i = n; i > 0; i--) {
            for (int j = 0; j < l; j++) {
                if (a[i][j] > num) {
                    allZero &= (j == 0);
                    if (!allZero) {
                        sb.append(digits.charAt(j));
                        if (j >= k && i > 1) {
                            String s = Integer.toString(num, l);
                            while (s.length() < i - 1) {
                                s = "0" + s;
                            }
                            sb.append(s);
                            break outer;
                        }
                    }
                    break;
                }
                num -= a[i][j];
            }
        }

        if (sb.length() == 0) {
            sb.append("0");
        }
        out.println(new BigInteger(sb.toString(), l));
        out.flush();
    }

    public void run() {
        try {
            solve();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}