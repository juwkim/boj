# [Silver V] Cash Gap - 19719 

[문제 링크](https://www.acmicpc.net/problem/19719) 

### 성능 요약

메모리: 114408 KB, 시간: 132 ms

### 분류

그리디 알고리즘(greedy), 구현(implementation), 시뮬레이션(simulation), 정렬(sorting)

### 문제 설명

<p>A recently founded "NERC" (New Era Russian Coders) company, of course, has an accounting department. And they are very concerned about the budget of the company. In particular, they don't want the company to experience a <em>cash gap</em> --- a condition where they need to pay more money than they have in their account now.</p>

<p>At the moment the company has $s$ euros on its account. The chief accountant has prepared a plan of transactions for $m$ following days. During this period $n$ transactions are planned.</p>

<p>For each transaction the change it makes to the company's account is known, but the exact date of the operation is unknown. Money transferred by clients may not be credited to the account immediately, and on the other hand, a claim to pay a bill can suddenly be received. For each transaction, only the range of days the transaction can happen is known in advance. If several transactions would happen on the same day, they can be performed in any order.</p>

<p>Help the accounting department to check if there exists an order of transactions such that the company will experience a cash gap. </p>

### 입력 

 <p>The first line contains integers $n$, $m$ and $s$ --- the number of payments, the number of days in the plan and the initial amount of money the company has ($1 \leqslant n, m \leqslant 1000$; $1 \leqslant s \leqslant 10^6$).</p>

<p>The $i$-th of the following $n$ lines contains a description of the $i$-th payment in the following format: "$\mathtt{count}~\mathtt{from}~\mathtt{to}$", which means that on any day from $\mathtt{from}$ to $\mathtt{to}$, the amount of money will be changed by $\mathtt{count}$ euros ($-10^6 \leqslant \mathtt{count} \leqslant 10^6$; $1 \leqslant \mathtt{from} \leqslant \mathtt{to} \leqslant m$).</p>

### 출력 

 <p>Print "<code>YES</code>" if a cash gap can occur, or "<code>NO</code>" if such situation is impossible.</p>

