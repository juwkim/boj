# [Silver I] Time Warp - 10393 

[문제 링크](https://www.acmicpc.net/problem/10393) 

### 성능 요약

메모리: 111336 KB, 시간: 144 ms

### 분류

많은 조건 분기, 기하학, 구현, 수학

### 제출 일자

2025년 8월 4일 03:34:57

### 문제 설명

<p>Tim Ang is a bit of a nerd. Check that – he’s a HUGE nerd. When you ask him the time, he might say something like “20 after 8”, which seems normal, but other times he’ll say things like “90 after 8” or “126 til 4”, which gives you pause. When you ask him about this, Tim say that “20 after 8” means the first time after 8 that the hour and minute hands of the clock make an angle of 20 degrees; “126 til 4” means the closest time before 4 that the hands make an angle of 126 degrees. As Tim walks away snickering, you resolve that you will write a program that will automatically convert Tim’s times to our more normal, non-nerdy times. That’ll show the little geek!</p>

### 입력 

 <p>The input file starts with an integer n indicating the number of test cases. Each test case consists of a single line of the form a after b or a til b, where a and b are integers satisfying 0 ≤ a < 360, and 1 ≤ b ≤ 12. All angles are measured starting at the hour hand and moving clockwise until reaching the minute hand (so, for example, at 9 o’clock the hands make an angle of 90 degrees and at 3 o’clock they make an angle of 270).</p>

### 출력 

 <p>For each test case, output the time in the format h:m:s, where h, m and s are the hour, minutes and seconds closest to the given angle and hour and 1 ≤ h ≤ 12. Always use two digits to represent the number of minutes and seconds.</p>

