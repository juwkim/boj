# [Silver II] Rate of Return - 9180 

[문제 링크](https://www.acmicpc.net/problem/9180) 

### 성능 요약

메모리: 110900 KB, 시간: 104 ms

### 분류

이분 탐색

### 제출 일자

2025년 3월 14일 04:13:25

### 문제 설명

<p>Jill has been investing in a mutual fund for a while. Since her income has varied, the amount of money she has added to the investment has varied, and she hasn’t always added to the investment at regular intervals. Nevertheless, she does have a complete record of the amounts she has invested, and the dates of those investments.</p>

<p>Periodically Jill gets a report that indicates the total value of her investment. She wonders if she would have done better by investing her money in a savings account that pays a fixed interest rate. But to determine the answer to this question, she needs to know what the equivalent interest rate would have been paid on the mutual fund, had it paid a fixed rate. You are going to help her.</p>

<p>For simplicity we will assume that Jill added money to her mutual fund only at the beginning of a month, and that all months have the same length. We will further assume that the interest she would have been paid had she invested in a savings account would have been paid at the end of the month, and would have been compounded monthly.</p>

<p>Let’s consider a simple example. Suppose Jill invested \$100 at the beginning of January and another \$100 in March. At the end of April she finds that the value of her mutual fund is \$210. If the equivalent fixed monthly interest rate was i, then we know that at the end of January the value would have been 100 × (1 + i). At the end of February the value would have been 100 × (1 + i) × (1 + i), or 100 × (1 + i)<sup>2</sup>. At the end of March, the value would have been 100 × (1 + i)<sup>3</sup> + 100 × (1 + i), and at the end of April, the value would have been 100 × (1 + i)<sup>4</sup> + 100 × (1 + i)<sup>2</sup>. So the question to be answered in this case is this: what is the value of i such that 100 × (1 + i)<sup>4</sup> + 100 × (1 + i)<sup>2</sup> = 210? The answer for this case is close to 0.016351795234.</p>

### 입력 

 <p>The input will contain multiple cases. The input for each case will begin with an integer N (no larger than 12) that indicates the number of times Jill invested in her mutual fund. This will be followed by N + 1 pairs, each pair containing an integer and a real number. The integer represents a month number (1 or larger) and the real number represents a dollar amount. The first N pairs give the month and amount of each of Jill’s N investments in the mutual fund, and the last pair indicates the value of the investment at the end of the specified month. There will be one or more whitespace characters (blanks, tabs, and/or ends of lines) between the input numbers. You may assume that the month numbers are given in ascending order.</p>

<p>Input for the last case will be followed by a single integer –1.</p>

### 출력 

 <p>For each case, display the case number (they start with 1 and increase sequentially) and the equivalent fixed monthly interest rate Jill’s mutual fund would have paid. Display this number with five fractional digits, rounded to the nearest decimal place. You may assume the interest rate will be no less than 0 and no larger than 1. Separate the output for consecutive cases by a blank line.</p>

