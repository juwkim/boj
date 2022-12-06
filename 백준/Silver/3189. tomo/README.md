# [Silver IV] tomo - 3189 

[문제 링크](https://www.acmicpc.net/problem/3189) 

### 성능 요약

메모리: 29200 KB, 시간: 252 ms

### 분류

구현(implementation), 수학(math), 정수론(number_theory), 비둘기집 원리(pigeonhole_principle), 시뮬레이션(simulation)

### 문제 설명

<p>The most advanced feature of Tom’s old calculator is that when he multiplies two numbers and continues to press the button '=', calculator continues to multiply the displayed number with the second of the two entered numbers. For example, if he multiplies 2 and 3, the number 6 will appear on the display. Further pressing the button '=' will result in numbers 18, 54, 162, etc. being displayed. </p>

<p>Tom is playing one interesting game – he wants to know how many times does he need to press the '=' button in order for some given number to appear as suffix of the number displayed on the calculator. </p>

<p>More precisely, Tom enters a number A, presses the button '*', enters the number B and presses the button '='. After that, product of the numbers A and B appears on the display. If the number C is not a suffix of the number displayed, Tom continues to press the button '=', until a number whose suffix is C is displayed. </p>

<p>We say that number X is suffix of number Y if the decimal representation of number Y ends with the decimal representation of number X (for example, 46 is suffix of 1246, but 70 is not suffix of 4701). We assume that the calculator can handle numbers with arbitrary many digits and that it can display all those digits. </p>

<p>Write a program that will, given numbers A, B and C, calculate the total number of times the button '=' will be pressed. </p>

### 입력 

 <p>First and only line of input contains integers A, B and C, 0 ≤ A, C ≤ 100,000, 0 ≤ B ≤ 1000. There will be no leading zeros in the representation of number C. </p>

### 출력 

 <p>First and only line of output should contain the number of times the button '=' will be pressed, or the word 'NIKAD' if there is no solution. </p>

