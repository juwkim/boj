#include <stdio.h>

int gcd(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

int v_factor(int n, int p, int *exp) {
    int c = 0;
    while (n % p == 0) {
        n /= p;
        ++c;
    }
    *exp = c;
    return n;
}

int powmod(int a, int e, int mod) {
    long long r = 1 % mod;
    long long base = a % mod;
    while (e) {
        if (e & 1) r = r * base % mod;
        base = base * base % mod;
        e >>= 1;
    }
    return (int)r;
}

int euler_phi(int n) {
    if (n == 1) return 1;
    int res = n, x = n;
    for (int d = 2; d * d <= x; ++d) {
        if (x % d == 0) {
            while (x % d == 0) x /= d;
            res -= res / d;
        }
    }
    if (x > 1) res -= res / x;
    return res;
}

void factorize(int n, int primes[], int exps[], int *cnt) {
    *cnt = 0;
    for (int d = 2; d * d <= n; ++d) {
        if (n % d == 0) {
            int c = 0;
            while (n % d == 0) { n /= d; ++c; }
            primes[*cnt] = d; exps[*cnt] = c; ++(*cnt);
        }
    }
    if (n > 1) {
        primes[*cnt] = n;
        exps[*cnt] = 1;
        ++(*cnt);
    }
}

int multiplicative_order_10(int m) {
    int phi = euler_phi(m);
    int d = phi;
    int primes[32]; int exps[32], pcnt = 0;
    factorize(phi, primes, exps, &pcnt);
    for (int i = 0; i < pcnt; ++i) {
        int p = primes[i];
        while (d % p == 0 && powmod(10, d / p, m) == 1)
            d /= p;
    }
    return d;
}

int main() {
    int x, y;
    while (1) {
        scanf("%d %d", &x, &y);
        if (x == 0) break;
        int a, b;
        int m = v_factor(v_factor(y / gcd(x, y), 2, &a), 5, &b);
        int cycle = m == 1 ? 0 : multiplicative_order_10(m);
        printf("%d %d\n", a > b ? a : b, cycle);
    }
    return 0;
}