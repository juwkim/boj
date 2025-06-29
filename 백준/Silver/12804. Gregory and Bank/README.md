# [Silver I] Gregory and Bank - 12804 

[문제 링크](https://www.acmicpc.net/problem/12804) 

### 성능 요약

메모리: 110908 KB, 시간: 124 ms

### 분류

그리디 알고리즘, 정렬

### 제출 일자

2025년 6월 30일 01:16:46

### 문제 설명

<p>Gregory is working in the accountant office of one big corporation. He gets money via wire transfers from company clients and sends money via wire transfers to company suppliers.</p>

<p>All transfers are processed using the only bank office in the city. The office has very strange schedule. Each day the bank allows just one type of operations: send wire transfers, or receive wire transfers. Additionally, Gregory can only do at most one operation each day: either send one transfer, or receive one transfer (depending on the operation type allowed on the corresponding day). The other party of the transfer can be chosen arbitrarily. Gregory's boss doesn't like Gregory to do nothing, so he insists that each day he goes to the bank and attempts to make some operations.</p>

<p>Gregory must process n requests of receiving money from clients and m request of sending money to suppliers. Gregory knows the schedule of the bank office. For each client or supplier he can set the day of the transfer.</p>

<p>Initially the bank account managed by Gregory has no money. Each day Gregory comes to the bank and either receives money to the account, or sends money from the account. Unfortunately it is possible that there are less money at the account than he needs to send. In such case he cannot pay to the supplier, so the transfer is cancelled, no money is sent, and Gregory gets a rebuke. The supplier refuses to continue operations with Gregory's company, so the transaction cannot be performed later.</p>

<p>Gregory wants to arrange wire transfers from clients and to suppliers in such way that the number of suppliers that he cannot actually send money was minimal. Help him!</p>

### 입력 

 <p>Input data contains several test cases. The first line of the input data contains the number of test cases t (1 ≤ t ≤ 1000).</p>

<p>Each test is described in the following way: the first line contains two integers: n and m (1 ≤ n, m ≤ 100) — the number of clients and the number of suppliers. The second line contains n integers a<sub>i</sub> (1 ≤ a<sub>i</sub> ≤ 1000) — the amounts that the i-th client must send to Gregory's company. The third line contains m integers b<sub>j</sub> (1 ≤ b<sub>j</sub> ≤ 1000) — the amount that must be sent to the j-th supplier. The following line contains a string s (length of s is n + m, it contains n characters "+" and m characters "-"). The character s[k] is "+" if on the k-th day the bank allows to receive money, and "-" if on the k-th day the bank allows to send money.</p>

### 출력 

 <p>For each test case print one integer: the minimal number of suppliers that Gregory would not send money to.</p>

