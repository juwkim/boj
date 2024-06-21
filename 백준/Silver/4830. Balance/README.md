# [Silver III] Balance - 4830 

[문제 링크](https://www.acmicpc.net/problem/4830) 

### 성능 요약

메모리: 108080 KB, 시간: 112 ms

### 분류

구현, 수학, 시뮬레이션

### 제출 일자

2024년 6월 21일 23:43:11

### 문제 설명

<p>An investor invests a certain percentage of his assets into NINSTRUMENTS financial instruments. After each term, these instruments deduct a certain fixed administrative cost, followed by a fee that is a percentage of the amount that was invested at the beginning of the term, and then add a return, which is a (positive or negative) percentage of the amount invested at the beginning of the term. If any account drops to zero or below after such a transaction, it is considered closed (no fees are charged against it, and is treated as simply zero) until a rebalancing occurs.</p>

<p>Rebalancing occurs after every NREBALANCE terms, where the total assets of the investor are redistributed according to the original ratios for the instruments. Without rebalancing, the investor's assets would become dominated by the higher return instruments, which would expose them to more risk compared to a balanced investment plan. Note that it is possible that all instruments drop to zero, in which case they all remain closed for the remaining terms.</p>

<p>You are to model the value of such an investment strategy and report the ending value in each instrument (before rebalancing, if it happens to land on a term when a rebalance is due). Compute your results using double precision (do not round intermediate values to pennies), but round your final answers to pennies.</p>

### 입력 

 <p>The first line of the input contains the three positive integers:</p>

<pre>NINSTRUMENTS NTERMS NREBALANCE</pre>

<p>There are no more than 10 instruments, and the number of terms is at most 20. This is followed by 3 lines of floating-point numbers separated by spaces, in the following format:</p>

<pre>FIXED_FEE(1) .. FIXED_FEE(NINSTRUMENTS)
PERCENTAGE_FEE(1) .. PERCENTAGE_FEE(NINSTRUMENTS)
PRINCIPAL_START(1) .. PRINCIPAL_START(NINSTRUMENTS)</pre>

<p>Finally, there are NTERMS lines each containing NINSTRUMENTS floating-point numbers indicating the percentage return of each instrument in each term:</p>

<pre>RETURN(1,1) .. RETURN(1,NINSTRUMENTS)
RETURN(2,1) .. RETURN(2,NINSTRUMENTS)
.
.
RETURN(NTERMS,1) .. RETURN(NTERMS,NINSTRUMENTS)</pre>

<p>All percentages (PERCENTAGE_FEE and RETURN) are given as ratios, up to 4 decimal places. For example, a fee of 0.0002 means 0.02% of the investment in this instrument is deducted as a fee each term. FIXED_FEE and PRINCIPAL_START are non-negative floating-point numbers that are specified to 2 decimal places. At least one of the PRINCIPAL_START values is positive.</p>

### 출력 

 <p>Write on a single line the principal of each investment (separated by a space) at the end of NTERMS terms. Round each principal to the nearest penny.</p>

<pre>PRINCIPAL_END(1) .. PRINCIPAL_END(NINSTRUMENTS)</pre>

