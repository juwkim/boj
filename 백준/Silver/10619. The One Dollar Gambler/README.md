# [Silver I] The One Dollar Gambler - 10619 

[문제 링크](https://www.acmicpc.net/problem/10619) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

수학, 확률론, 기댓값의 선형성

### 제출 일자

2025년 8월 15일 13:57:25

### 문제 설명

<p>Starting with one dollar of capital, a gambler chooses a fixed proportion, F, of his capital to bet on a fair coin toss repeatedly for T tosses.</p>

<p>His return is double his bet for heads and he loses his bet for tails.</p>

<p>For example, if F=1/4, for the first toss he bets 0.25<span>$</span>, and if heads comes up he wins 0.5<span>$</span> and so then have 1.5<span>$</span>. He then bets 0.375<span>$</span> and if the second toss is tails, he has 1.125<span>$</span> left.</p>

<p><img alt="" src="" style="float:right; height:255px; width:228px">The diagram on the right shows the possibilities in two coin tosses. If both times head comes, his worth is 2.25<span>$</span>, if one head and one tail comes in either order, his worth is 1.125<span>$</span>, and in case it is tails both times, he is left with 0.5625<span>$</span>. All four cases are equally probable. The expected worth of the one dollar gambler is therefore 1.265625 after a two toss game.</p>

<p>Your task in this problem is to find the expected worth of the one dollar gambler given F, the fraction of current worth to bet on the next toss and T, the total number of coin tosses.</p>

### 입력 

 <p>The input consists of multiple test cases. The first line of input is the number of test cases N (1≤N≤100). Each of the following N lines contains a float point number F (0≤F≤1), the fraction of current worth to bet and T (1≤T≤100), the number of coin tosses.</p>

### 출력 

 <p>For each test case, print a single line saying “Case #n:” where n is the test case number followed by a space followed by the expected worth of the one dollar gambler. Small absolute or relative errors(10<sup>-6</sup>) are acceptable in the output.</p>

