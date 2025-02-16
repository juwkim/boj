# [Silver II] Holiday Costing - 8009 

[문제 링크](https://www.acmicpc.net/problem/8009) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

구현, 수학

### 제출 일자

2025년 2월 16일 17:17:19

### 문제 설명

<p>Resort hotels often offer "stay/pay" deals where after so many nights you get some nights free. For example, in a stay 8 / pay 7 deal, if you stay 8 nights then you only pay for 7 (one is free). If you stay 9 then you pay for 8. Often these deals can accumulate. For example, a stay 6 pay 4 deal that can be repeated three times means that stay 12 pay 8 and stay 18 pay 12 deals also exist. Some hotels offer multiple stay pay deals, however these cannot be combined.</p>

<p>Write a program that will calculate the best rate for a given stay, i.e. that will choose the best (possibly repeated) deal for a given length of stay.</p>

### 입력 

 <p>Input consists of a number of sets of data, each relating to one hotel. The first line for each hotel is the name of the hotel, a sequence of up to 20 characters, possibly including spaces. This is followed by between 0 and 10 lines of stay/pay deals. Each stay/pay deal consists of three integers in the range 1 to 99: stay, pay, number of repeats. The stay/pay section is terminated by a line consisting of three zeroes (0 0 0). Following the stay/pay section is a series of integers, one per line, indicating some number of nights (also in the range 1 to 99), terminated by a line containing a single 0. This line should not be processed. The sequence of hotels is terminated by a line consisting of a single #.</p>

### 출력 

 <p>Output consists of one line for each number of nights in the input, indicating the minimum number of nights that have to be paid for. Note that this minimum must be made up of a combination of standard deals (pay for as many nights as you stay) and at most one stay/pay deal, repeated if necessary. Match the sample output format given below.</p>

