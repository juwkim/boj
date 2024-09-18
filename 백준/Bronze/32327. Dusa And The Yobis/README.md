# [Bronze III] Dusa And The Yobis - 32327 

[문제 링크](https://www.acmicpc.net/problem/32327) 

### 성능 요약

메모리: 110836 KB, 시간: 124 ms

### 분류

사칙연산, 구현, 수학, 시뮬레이션

### 제출 일자

2024년 9월 18일 16:02:23

### 문제 설명

<p>Dusa eats Yobis, but only Yobis of a certain size.</p>

<p>If Dusa encounters a Yobi that is smaller than itself, it eats the Yobi, and absorbs its size. For example, if Dusa is of size 10 and it encounters a Yobi of size 6, Dusa eats the Yobi and expands to size 10 + 6 = 16.</p>

<p>If Dusa encounters a Yobi that is the same size as itself or larger, Dusa runs away without eating the Yobi.</p>

<p>Dusa is currently facing a line of Yobis and will encounter them in order. Dusa is guaranteed to eventually encounter a Yobi that causes it to run away. Your job is to determine Dusa’s size when this happens.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/abfc008e-a912-44bb-9183-eecfaccd9631/-/preview/" style="width: 373px; height: 100px;"></p>

### 입력 

 <p>The first line of input contains a positive integer, D, representing Dusa’s starting size.</p>

<p>The remaining lines of input contain positive integers representing the sizes of the Yobis in order.</p>

### 출력 

 <p>Output the positive integer, R, which is Dusa’s size when it eventually runs away.</p>

