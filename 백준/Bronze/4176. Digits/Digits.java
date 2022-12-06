import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder out = new StringBuilder();

        while (true) {
            String s = in.readLine();
            if (s.equals("END")) break;

            if (s.length() == 1) {
                if (s.equals("1")) out.append("1\n");
                else out.append("2\n");
                continue;
            }

            int ans = 2, now = s.length();
            for (int nxt = (now + "").length(); now != nxt; ++ans) {
                now = nxt;
                nxt = (now + "").length();
            }

            out.append(ans + "\n");
        }

        System.out.println(out);
    }
}