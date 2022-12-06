# [Bronze III] Questionnaire - 18964 

[문제 링크](https://www.acmicpc.net/problem/18964) 

### 성능 요약

메모리: 4528 KB, 시간: 0 ms

### 분류

애드 혹(ad_hoc), 수학(math)

### 문제 설명

<p>In order to get better results in official ACM ICPC contests, the team leader came up with a questionnaire. He asked every participant whether they want to have more training.</p>

<p>Obviously, many people don't want more training, so the clever leader didn't write down their words such as "Yes" or "No". Instead, he let everyone choose a positive integer $a_i$ to represent their opinion. Amazingly, all the resulting numbers were distinct.</p>

<p>Now the leader wants to choose a pair of positive intergers $m$ ($1 < m \le 10^9$) and $k$ ($0 \le k < m$), and regard those people whose number is exactly $k$ modulo $m$ as "Yes",  and all others as "No". If there are at least as many "Yes" answers as "No" answers, the leader can have a chance to offer more training.</p>

<p>Please help the team leader to find such pair of $m$ and $k$.</p>

### 입력 

 <p>The first line of the input contains an integer $n$: the number of ACM ICPC participants ($3 \leq n \leq 10^5$).</p>

<p>The next line contains $n$ distinct integers $a_1$, $a_2$, $\ldots$, $a_n$: the numbers chosen by the participants ($1 \leq a_i \leq 10^9$).</p>

### 출력 

 <p>Print a single line containing two integers $m$ and $k$. If there are several possible solutions, print any one of them.</p>

