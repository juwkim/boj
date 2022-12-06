# [Silver V] Contaminated Milk - 11972 

[문제 링크](https://www.acmicpc.net/problem/11972) 

### 성능 요약

메모리: 30840 KB, 시간: 112 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>Farmer John, known far and wide for the quality of the milk produced on his farm, is hosting a milk-tasting party for \(N\) of his best friends (\(1 \leq N \leq 50\)). Unfortunately, of the \(M\) types of milk featured at the party (\(1 \leq M \leq 50\)), exactly one of them has gone bad, but Farmer John does not know which one! Anyone who drinks the bad milk will later become sick, either during the remainder of the party or afterward.</p>

<p>You are given a transcript of the party -- who drinks what when, and also who gets sick when. Based on this information, you can deduce which of the milks could possibly be the bad one. Using this knowledge, help Farmer John determine the minimum number of doses of medicine he will need to obtain in order to guarantee that he can cure all of the individuals who become sick, either during or after the party.</p>

### 입력 

 <p>The first line of the input contains integers \(N\), \(M\), \(D\), and \(S\).</p>

<p>The next \(D\) lines (\(1 \leq D \leq 1000\)) each contain three integers \(p, m, t\), indicating that person \(p\) drank milk \(m\) at time \(t\). The value of \(p\) is in the range \(1 \ldots N\), \(m\) is in the range \(1 \ldots M\), and \(t\) is in the range \(1 \ldots 100\). A person may drink the same milk several times, and may also drink several types of milk at the same point in time.</p>

<p>The next \(S\) lines (\(1 \leq S \leq N\)) each contain two integers \(p, t\), indicating that person \(p\) gets sick at time \(t\). The value of \(p\) is in the range \(1 \ldots N\), and \(t\) is in the range $1 \ldots 100$. Each person gets sick at most once, and they only get sick because they drank the bad milk at some strictly earlier point in time.</p>

### 출력 

 <p>A single integer, specifying the minimum number of doses of medicine Farmer John needs to obtain so that he can guarantee that he will have sufficiently many doses to treat all the people who become sick, both during and after the party.</p>

