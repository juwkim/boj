#include <bits/stdc++.h>
using namespace std;

const int MAXI = 5e5 + 7;
int schody[MAXI];

int binarysearchpowyniku(int pocz, int kon, int co){
    int sro;
    while(pocz < kon){
        sro = (pocz + kon + 1) / 2;
        if(schody[sro] <= co){
            pocz = sro;
        }
        else{
            kon = sro - 1;
        }
    }
    return pocz;
}

int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n, m, maxi = 0, osoba, wyn;
    cin >> n >> m;
    for(int i = 1; i <= n; i++){
        cin >> schody[i];
        if(schody[i] > maxi){
            maxi = schody[i];
        }
        schody[i] = maxi + 1;
    }
    for(int i = 1; i <= m; i++){
        cin >> osoba;
        if(osoba < schody[1]){
        	cout << 0 << ' ';
        	continue;
        }
        if(osoba >= schody[n]){
        	cout << n << ' ';
        	continue;
        }
        wyn = binarysearchpowyniku(1, n, osoba);
        cout << wyn << ' ';
    }
    cout << '\n';
    return 0;
}