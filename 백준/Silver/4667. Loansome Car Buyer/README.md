# [Silver II] Loansome Car Buyer - 4667 

[문제 링크](https://www.acmicpc.net/problem/4667) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

구현, 수학, 시뮬레이션

### 제출 일자

2025년 3월 11일 00:17:18

### 문제 설명

<p>Kara Van and Lee Sabre are lonesome. A few months ago they took out a loan to buy a new car, but now they're stuck at home on Saturday night without wheels and without money. You see, there was a wreck and the car was totaled. Their insurance paid <span>$</span>10,000, the current value of the car. The only problem is that they owed the bank <span>$</span>15,000, and the bank wanted payment immediately, since there was no longer a car for collateral. In just a few moments, this unfortunate couple not only lost their car, but lost an additional <span>$</span>5,000 in cash too.</p>

<p>What Kara and Lee failed to account for was depreciation, the loss in value as the car ages. Each month the buyer's loan payment reduces the amount owed on the car. However, each month, the car also depreciates as it gets older. Your task is to write a program that calculates the first time, measured in months, that a car buyer owes less money than a car is worth. For this problem, depreciation is specified as a percentage of the previous month's value.</p>

### 입력 

 <p>Input consists of information for several loans. Each loan consists of one line containing the duration in months of the loan, the down payment, the amount of the loan, and the number of depreciation records that follow. All values are nonnegative, with loans being at most 100 months long and car values at most <span>$</span>75,000. Since depreciation is not constant, the varying rates are specified in a series of depreciation records. Each depreciation record consists of one line with a month number and depreciation percentage, which is more than 0 and less than 1. These are in strictly increasing order by month, starting at month 0. Month 0 is the depreciation that applies immediately after driving the car off the lot and is always present in the data. All the other percentages are the amount of depreciation at the end of the corresponding month. Not all months may be listed in the data. If a month is not listed, then the previous depreciation percentage applies. The end of the input is signalled by a negative loan duration - the other three values will be present but indeterminate.</p>

<p>For simplicity, we will assume a 0% interest loan, thus the car's initial value will be the loan amount plus the down payment. It is possible for a car's value and amount owed to be positive numbers less than <span>$</span>1.00. Do not round values to a whole number of cents (<span>$</span>7,347.635 should not be rounded to <span>$</span>7,347.64).</p>

<p>Consider the first example below of borrowing <span>$</span>15,000 for 30 months. As the buyer drives off the lot, he still owes <span>$</span>15,000, but the car has dropped in value by 10% to <span>$</span>13,950. After 4 months, the buyer has made 4 payments, each of <span>$</span>500, and the car has further depreciated 3% in months 1 and 2 and 0.2% in months 3 and 4. At this time, the car is worth <span>$</span>13,073.10528 and the borrower only owes <span>$</span>13,000.</p>

### 출력 

 <p>For each loan, the output is the number of complete months before the borrower owes less than the car is worth. Note that English requires plurals (5 months) on all values other than one (1 month).</p>

