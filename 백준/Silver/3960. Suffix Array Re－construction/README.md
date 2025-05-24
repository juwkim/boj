# [Silver I] Suffix Array Re-construction - 3960 

[문제 링크](https://www.acmicpc.net/problem/3960) 

### 성능 요약

메모리: 177992 KB, 시간: 796 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 5월 24일 19:37:13

### 문제 설명

<p>It has been a long day at your new job. You have spent all day optimizing the most important Suffix-Array data structures your new employer, the GCPC ([G]lobal Suffix [C]ollecting and [P]rocessing [C]ollective),works with. The moment you were just about to shut down your workstation you stop and stare at the monitor. Your test run just has revealed that large portions of the important data must be corrupted. Sadly, the Company’s backup servers just crashed yesterday, and now you may have destroyed the valuable Suffix-Arrays.</p>

<p>On inspecting the data, you find that it could hardly be worse. A lot of the suffixes are missing and even the ones remaining might be broken. You have found examples wherein parts of the letters have been replaced by random letters, and in some parts you find a single ’*’, your placeholder character you used in the software. This placeholder has replaced an arbitrarily large substring. Furthermore, you found some inconsistent strings, for which it is not clear which version of the character is the right one. Your only chance now is to hope and pray that a recovery is possible.</p>

<p>The data is given as a list of suffixes, together with the start-position of the suffix. You also still have a list of the length of all the data-sets the company has in stock. Can you possibly reconstruct at least the base strings? If so, one could run one of those fancy new Suffix-Array algorithms to reconstruct the full data-set again.</p>

### 입력 

 <p>Each test set consists of multiple test cases t (0 < t ≤ 100). The number of test cases is given on a single line at the beginning of the input. Every test case is composed as follows. First, on a single line, the length l of the desired output string is given, together with the number of (partially broken) suffixes s (1 ≤ l ≤ 10 000; 1 ≤ s ≤ 10 000). Then s lines follow, giving the position p of the suffix in the string and the suffix (1 ≤ p ≤ l). The suffix will contain only characters from the set of {a, ... , z, A, ... , Z, ., ∗} (the ’.’ has no special meaning). The total sum of characters given for the suffixes will not exceed 250 000.</p>

### 출력 

 <p>Whenever it is possible to reconstruct the lost input data print the reconstructed sentence, else print “IMPOSSIBLE” on a single line. For our case, the recovery is only possible if the set of possible characters for a position in the string contains exactly one character.</p>

