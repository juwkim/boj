# [Bronze III] Combination Lock - 4327 

[문제 링크](https://www.acmicpc.net/problem/4327) 

### 성능 요약

메모리: 30840 KB, 시간: 156 ms

### 분류

구현(implementation), 수학(math)

### 문제 설명

<p>Now that you're back to school for another term, you need to remember how to work the combination lock on your locker. A common design is that of the Master Brand, shown at right. The lock has a dial with 40 calibration marks numbered 0 to 39. A combination consists of 3 of these numbers; for example: 15-25-8. To open the lock, the following steps are taken:</p>

<ul>
	<li>turn the dial clockwise 2 full turns</li>
	<li>stop at the first number of the combination</li>
	<li>turn the dial counter-clockwise 1 full turn</li>
	<li>continue turning counter-clockwise until the 2nd number is reached</li>
	<li>turn the dial clockwise again until the 3rd number is reached</li>
	<li>pull the shank and the lock will open.</li>
</ul>

<p>Given the initial position of the dial and the combination for the lock, how many degrees is the dial rotated in total (clockwise plus counter-clockwise) in opening the lock?</p>

### 입력 

 <p>Input consists of several test cases. For each case there is a line of input containing 4 numbers between 0 and 39. The first number is the position of the dial. The next three numbers are the combination. Consecutive numbers in the combination will be distinct. A line containing 0 0 0 0 follows the last case.</p>

### 출력 

 <p>For each case, print a line with a single integer: the number of degrees that the dial must be turned to open the lock.</p>

