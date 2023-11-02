# [Silver IV] HST - 4166 

[문제 링크](https://www.acmicpc.net/problem/4166) 

### 성능 요약

메모리: 144376 KB, 시간: 452 ms

### 분류

사칙연산, 자료 구조, 해시를 사용한 집합과 맵, 수학, 파싱, 문자열

### 제출 일자

2023년 11월 2일 14:17:21

### 문제 설명

<p>On July 1st, Ontario's Provincial Sales Tax (PST) was merged with the Federal Goods and Services Tax (GST), creating the Harmonized Sales Tax (HST). This changed the rate of tax Ontarians pay on various items.</p>

<p>Dalton would like to calculate how this change will affect his personal monthly budget.</p>

### 입력 

 <p>The first line of input contains a single integer, the number of test cases to follow. Each test case begins with a line containing two integers N, M, the number of categories of items and the number of purchases Dalton makes each month, respectively. Each of these integers is between 1 and 100000, inclusive. N lines follow, each describing a category of item. Each of these lines contains a category name, which is a string of at most 30 uppercase letters, followed by three percentages, giving the PST, GST, and HST rate on that category. Each percentage is a number with up to two digits after the decimal point, and each percentage is followed by the % symbol. Each percentage is at least 0% and at most 100%. These lines are followed by M more lines, each describing one of Dalton's purchases. Each of these lines contains a category name and a price in dollars and cents and prefixed by the <span>$</span> symbol. Each such line indicates the amount of pre-tax money that Dalton spends on an item in the specified category. The amount of each tax to be paid on an item is rounded to the nearest cent; if the tax amount is exactly half a cent more than a whole number of cents, it is rounded up to the nearest greater whole number of cents.</p>

### 출력 

 <p>For each test case, output the difference, in dollars and cents, between the total HST payable and the total sum of PST and GST payable on Dalton's monthly purchases. If the HST is more than the PST+GST, output a positive amount. If the HST is less than the PST+GST, output a negative amount.</p>

