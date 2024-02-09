# [Silver III] Skyscraper “MinatoHarukas” - 16034 

[문제 링크](https://www.acmicpc.net/problem/16034) 

### 성능 요약

메모리: 109240 KB, 시간: 388 ms

### 분류

수학

### 제출 일자

2024년 2월 9일 23:38:20

### 문제 설명

<p>Mr. Port plans to start a new business renting one or more floors of the new skyscraper with one giga floors, MinatoHarukas. He wants to rent as many vertically adjacent floors as possible, because he wants to show advertisement on as many vertically adjacent windows as possible. The rent for one floor is proportional to the floor number, that is, the rent per month for the <i>n</i>-th floor is <i>n</i> times that of the first floor. Here, the ground floor is called the first floor in the American style, and basement floors are out of consideration for the renting. In order to help Mr. Port, you should write a program that computes the vertically adjacent floors satisfying his requirement and whose total rental cost per month is <em>exactly equal</em> to his budget.</p>

<p>For example, when his budget is 15 units, with one unit being the rent of the first floor, there are four possible rent plans, 1+2+3+4+5, 4+5+6, 7+8, and 15. For all of them, the sums are equal to 15. Of course in this example the rent of maximal number of the floors is that of 1+2+3+4+5, that is, the rent from the first floor to the fifth floor.</p>

### 입력 

 <p>The input consists of multiple datasets, each in the following format.</p>

<pre><i>b</i></pre>

<p>A dataset consists of one line, the budget of Mr. Port <i>b</i> as multiples of the rent of the first floor. <i>b</i>  is a positive integer satisfying 1 < <i>b</i> < 10<sup>9</sup>.</p>

<p>The end of the input is indicated by a line containing a zero. The number of datasets does not exceed 1000.</p>

### 출력 

 <p>For each dataset, output a single line containing two positive integers representing the plan with the maximal number of vertically adjacent floors with its rent price exactly equal to the budget of Mr. Port. The first should be the lowest floor number and the second should be the number of floors.</p>

