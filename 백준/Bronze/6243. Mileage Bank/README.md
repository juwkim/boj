# [Bronze III] Mileage Bank - 6243 

[문제 링크](https://www.acmicpc.net/problem/6243) 

### 성능 요약

메모리: 109544 KB, 시간: 96 ms

### 분류

사칙연산, 구현, 수학

### 제출 일자

2025년 1월 2일 21:08:42

### 문제 설명

<p>Mileage program of ACM (Airline of Charming Merlion) is really nice for the travelers flying frequently. Once you complete a flight with ACM, you can earn ACMPerk miles in your ACM Mileage Bank depended on mileage you actual fly. In addition, you can use the ACMPerk mileage in your Mileage Bank to exchange free flight ticket of ACM in future. </p>

<p>The following table helps you calculate how many ACMPerk miles you can earn when you fly on ACM. </p>

<pre>When you fly ACM         Class Code              You'll earn
First Class                   F         Actual mileage + 100% mileage Bonus
Business Class                B         Actual mileage + 50% mileage Bonus 
Economy Class                 Y
1-500 miles                                        500 miles
500+ miles                                       Actual mileage</pre>

<p>It's shown that your ACMPerk mileage consists of two parts. One is your actual flight mileage (the minimum ACMPerk mileage for Economy Class for one flight is 500 miles), the other is the mileage bonus (its accuracy is up to 1 mile) when you fly in Business Class and First Class. For example, you can earn 1329 ACMPerk miles, 1994 ACMPerk miles and 2658 ACMPerk miles for Y, B or F class respectively for the fly from Beijing to Tokyo (the actual mileage between Beijing and Tokyo is 1329 miles). When you fly from Shanghai to Wuhan, you can earn ACMPerk 500 miles for economy class and ACMPerk 650 miles for business class (the actual mileage between Shanghai and Wuhan is 433 miles). </p>

<p>Your task is to help ACM build a program for automatic calculation of ACMPerk mileage. </p>

### 입력 

 <p>The input file contains several data cases. Each case has many flight records, each per line. The flight record is in the following format: </p>

<pre>OriginalCity DistanceCity ActualMiles ClassCode </pre>

<p>Each case ends with a line of one zero. </p>

<p>A line of one # presents the end of the input file. </p>

### 출력 

 <p>Output the summary of ACMPerk mileages for each test case, one per line.</p>

