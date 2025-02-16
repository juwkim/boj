// Zadatak: BOMBONI
// Slozenost: O( Eratostenovo sito do R )
// Rjesenje napisao: Goran Zuzic

#include <algorithm>
#include <functional>

#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <string>
#include <vector>

using namespace std;

const int MAXR = 2000100;

int L, R;
int jelProst[ MAXR ];

int no_p;

vector< int > Prosti;

int NextP[ MAXR ];
int Djelitelja[ MAXR ];

int main( void )
{
    scanf( "%d %d", &L, &R );
    memset( jelProst, -1, sizeof jelProst );

    for( int i = 2; i <= R; ++i )
        if( jelProst[i] ) {
            Prosti.push_back( i );
            for( int j = i+i; j <= R; j += i )
                jelProst[j] = false;
        }

    NextP[1] = 0;
    Djelitelja[1] = 1;
    no_p = ( int )Prosti.size();

    for( long long i = 1; i <= R; ++i ) 
        for( int j = NextP[i]; j < no_p; ++j ) {
            long long k = i*Prosti[j];
            int korak = 1;

            if( k > R ) break;

            do { 
                ++korak;
                Djelitelja[k] = Djelitelja[i] * korak;
                NextP[k] = j+1;
                k *= Prosti[j];
            } while( k <= R );
        }
    
    int maks = 0;
    int cnt = 0;

    for( int i = L; i <= R; ++i )
        if( Djelitelja[i] > maks )
            maks = Djelitelja[i];
    
    for( int i = L; i <= R; ++i )
        if( Djelitelja[i] == maks )
            ++cnt;
    
    printf( "%d %d\n", maks, cnt );

    for( int i = L; i <= R; ++i )
        if( Djelitelja[i] == maks )
            printf( "%d\n", i );

    return (0-0);
}
