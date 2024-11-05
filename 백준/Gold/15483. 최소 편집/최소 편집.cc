#include <iostream>
#include <string>
#include <vector>
#include <algorithm> // std::min

int main() {
    std::string A, B;
    std::cin >> A >> B;
    
    int lenA = A.size();
    int lenB = B.size();
    
    std::vector<int> p(lenB + 1), c(lenB + 1);
    
    for (int j = 0; j <= lenB; j++) {
        p[j] = j;
    }
    
    for (int i = 0; i < lenA; i++) {
        c[0] = i + 1;
        for (int j = 0; j < lenB; j++) {
            int cost = (A[i] == B[j]) ? p[j] : 1 + std::min({c[j], p[j], p[j + 1]});
            c[j + 1] = cost;
        }
        std::swap(p, c);
    }
    
    std::cout << p[lenB] << std::endl;
    return 0;
}
