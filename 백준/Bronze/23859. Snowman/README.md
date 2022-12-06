# [Bronze I] Snowman - 23859 

[문제 링크](https://www.acmicpc.net/problem/23859) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

그리디 알고리즘(greedy), 문자열(string)

### 문제 설명

<p>Do you wanna build a snowman? Of course, you do! And you finally have enough snow on the walk in front of your house. But you see that snow on different sections of the walkway has different quality: on some sections, snow is good, white and sticky, let's say, such sections are class <strong>a</strong> sections, other sections with a bit worse quality would have class <strong>b</strong>, for even worse quality --- class <strong>c</strong> and so on.</p>

<p>To build a base for a snowman you should roll a snowball forward or backward from one track section to another. There is enough snow, so you can go back to the same section as many times as you want.  Of course, you want to build a snowman out of the best snow, and the closer to the centre of the snowball, the more important the quality of snow for the future snowman, so at the beginning of the building process you should choose the best sections. For example, if you roll a snowball starting on section with class <strong>c</strong>, then on section <strong>a</strong>, and then on section <strong>b</strong> (<strong>cab</strong>), it would not be as solid as the <strong>bab</strong> ball, and the <strong>aca</strong> snowball would be even better.</p>

<p>Classes of track sections are written in the string $s$. To make the first ball, you need to roll it through the track sections $k$ times. You can start to roll a ball for the snowman at any section of the track. What sequence of sections should be used to get the most solid ball?</p>

### 입력 

 <p>The first line contains the string $s$ of lowercase letters --- track sections classes. The number of sections is not less than 2 and not greater than 100.</p>

<p>The second line contains one integer $k$ ($1 \le k \le 10^4$) --- the number of sections for the snowball. </p>

### 출력 

 <p>Print the sequence of letters without spaces --- section classes in the order you will roll the ball.</p>

