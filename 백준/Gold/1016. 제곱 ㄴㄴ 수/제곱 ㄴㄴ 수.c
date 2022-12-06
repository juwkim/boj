#include <stdio.h>
#include <math.h>
#include <memory.h>
#include <malloc.h>
void get_prime_nums(long long* primes, long long N) {
    long long i, j;
    primes[0] = 0;
    primes[1] = 0;
    for (i=2; i*i<=N; i++) {
        if (primes[i]) {
            j = 2;
            while (i * j <= N) {
                primes[i*j] = 0;
                j++;
            }
        }
    }
}

int main()
{
    long long min, max, count, i;
    scanf("%lld %lld", &min, &max);
    count = max - min + 1;

    // find primes less than or equal to sqrt(max)
    long long primes_size = 1 + sqrt((double) max) / 1;
    long long primes[1000001];
    for (i=0; i < primes_size; i++) {
        primes[i] = 1;
    }
    get_prime_nums(primes, primes_size);

    long long sieve[1000001];
    for (i=0; i < max - min + 1; i++) {
        sieve[i] = 1;
    }

    for (i=2; i < primes_size; i++) {
        if (primes[i]) {
            long long sNum = min / (i * i);
            if (min % (i * i)) sNum++;
            
            long long cNum = sNum * (i * i);
            while (cNum <= max) {
                if (sieve[cNum - min]) {
                    sieve[cNum - min] = 0;
                    count--;
                }
                cNum = ++sNum * (i * i);
            }
            
        }
    }
    printf("%lld\n", count);
    return 0;
}