# [Silver IV] Paint - 9830 

[문제 링크](https://www.acmicpc.net/problem/9830) 

### 성능 요약

메모리: 111544 KB, 시간: 120 ms

### 분류

그리디 알고리즘, 정렬

### 제출 일자

2023년 10월 11일 17:08:13

### 문제 설명

<p>A junior college in Singapore just acquired a sailing boat, and the school’s student sailing team undertakes to paint the boat. There are several painting jobs to be done on the boat, such as:</p>

<ul>
	<li>primer painting on the keel,</li>
	<li>painting antifouling below the waterline,</li>
	<li>painting the deck,</li>
	<li>etc</li>
</ul>

<p>Each job can be started and finished on the same day, but in order for the paint to dry, at most one job can be done every day.</p>

<p>The students face the following problem. The supplier of paint charges a certain amount for the paint for each job, but is increasing the price every day by an amount that depends on the job. For example, he may charge <span>$</span>100 for the primer on the first day, and increase the price by <span>$</span>2 each day, resulting in a price of <span>$</span>102 on the second day, <span>$</span>104 on the third day, etc. For the antifouling, he may charge <span>$</span>200 on the first day, but increase the price by <span>$</span>4 each day, resulting in a price of <span>$</span>204 on the second day, <span>$</span>208 on the third day, etc. The students have no facilities for storing the paint, and therefore need to buy the paint on the day on which they use it. The students want to complete all jobs in the cheapest possible way.</p>

### 입력 

 <p>Your program must read from the standard input the following data. The first line of the input contains one integer, n, ranging from 2 to 20000, which specifies the number of painting jobs. We identify the jobs by numbers, ranging from job 1 to job n, regardless of when they are executed. The following line contains n numbers, each ranging from 1 to 1000. The i<sup>th</sup> number in this line specifies the price for the paint for job i. The last line contains n numbers, each ranging from 0 to 10. The j<sup>th</sup> number in this line specifies the amount of money by which the price for the paint for job j increases every day.</p>

### 출력 

 <p>The required output, to be written to standard output, consists of a single number, specifying the smallest amount of money sufficient to complete all jobs.</p>

