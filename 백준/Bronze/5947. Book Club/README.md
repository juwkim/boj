# [Bronze I] Book Club - 5947 

[문제 링크](https://www.acmicpc.net/problem/5947) 

### 성능 요약

메모리: 43644 KB, 시간: 1668 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>Bessie is looking for cows to join her book club. While the herd has N (2 <= N <= 50,000) cows conveniently numbered 1..N, she wants only the most discerning and social cows for her book club.</p>

<p>Thus, like a dating service, she has created a questionnaire and asked each of the N cows to complete its NQ (1 <= NQ <= 50) questions (named R_1..R_NQ). These are questions like "How much do you enjoy reading science fiction?" and each answer is an integer in the range 1..5.</p>

<p>Your job is to tabulate the questionnaire's results and answer a simple question like: "How many cows answered 2 to question 3, 4 to question 7, and also 1 to question 8?"  The question has P parts (1 <= P <= 10), and each part has Qj (1 <= Qj <= NQ) and Aj (1 <= Aj <= 5), respectively the question number and the required answer. Your program prints a single integer that is the total number of cows that answered Aj to Qj for j in the range 1..P.</p>

<p>Consider a small herd of just 4 cows and a small questionnaire of just 5 questions; the responses are:</p>

<pre>Cow     Question
 ID   1  2  3  4  5
 1    1  1  1  1  1
 2    1  2  3  4  5
 3    1  2  1  2  3
 4    2  1  1  2  2</pre>

<p>If the tabulation question was "How many cows answered 2 to question 1 and 1 to question 2?" the answer would be 1 (just cow #4). If the tabulation question was "How many cows answered 1 to question 1 and 1 to question 3?" the answer would be 2 (cows 1 and 3).</p>

### 입력 

 <ul>
	<li>Line 1: Three space-separated integers: N, NQ, and P</li>
	<li>Lines 2..N+1: Line i+1 contains NQ space-separated integers that are the response to the questions for cow i: R_1..R_NQ</li>
	<li>Lines N+2..N+1+P: Line j+N+1 contains two space-separated integers: Qj and Aj</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Line 1: A single integer that is the number of cows that meet all of Bessie's criteria​</li>
</ul>

