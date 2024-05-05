#include <unistd.h>
#include <string.h>
#define f() r[c++] = b[i++]

int main() {
	char r[2000000], b[1000001];
	int  i = 0, c = 0, s = read(0, b, 1000000);
	while (i < s) {
		switch (b[i]) {
		case ' ': ++i; continue;
		case '<': case '>': case '(': case ')': f(); break;
		case '&': case '|': f(); f(); break;
		default: while (strchr("<>()&| ", b[i]) == NULL) f();
		}
        r[c++] = ' ';
	}
	r[--c] = '\0';
    write(1, r, c);
}