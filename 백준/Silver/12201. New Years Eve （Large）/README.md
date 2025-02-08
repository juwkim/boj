# [Silver I] New Years Eve (Large) - 12201 

[문제 링크](https://www.acmicpc.net/problem/12201) 

### 성능 요약

메모리: 562556 KB, 시간: 11852 ms

### 분류

구현

### 제출 일자

2025년 2월 9일 07:17:42

### 문제 설명

<p>At new years party there is a pyramidal arrangement of glasses for wine. For example, at the top level, there would just be one glass, at the second level there would be three, then 6 and then 10 and so on and so forth like the following image. </p>

<p><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/12200/images.jpeg" style="height:228px; width:212px"></p>

<p>The glasses are numbered using 2 numbers, L and N. L represents the level of the glass and N represents the number in that level. Numbers in a given level are as follows:</p>

<pre>Level 1: 
    1

Level 2:
    1
 2     3

Level 3:
      1
   2     3
4     5     6

Level 4:
         1
      2     3
   4     5     6
7     8     9     10
</pre>

<p>Each glass can hold 250ml of wine. The bartender comes and starts pouring wine in the top glass(The glass numbered L = 1 and N = 1) from bottles each of capacity 750ml.</p>

<p>As wine is poured in the glasses, once a glass gets full, it overflows equally into the 3 glasses on the next level below it and touching it, without any wine being spilled outside. It doesn't overflow to the glasses on the same level beside it. It also doesn't overflow to the any level below next level (directly).</p>

<p>For example: When the glass of L = 2 and N = 2 overflows, the water will overflow to glasses of L = 3 and N = 2, 4, 5.</p>

<p>Once that the bartender is done pouring B bottles, figure out how much quantity in ml of wine is present in the glass on level L with glass number N.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <strong>T</strong>. <strong>T</strong> test cases follow. Each test case consists of three integers, <strong>B</strong>, <strong>L</strong>, <strong>N</strong>, <strong>B</strong> is the number of bottles the bartender pours and <strong>L</strong> is the glass level in the pyramid and <strong>N</strong> is the number of the glass in that level.</p>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where <strong>x</strong> is the test case number (starting from 1) and <strong>y</strong> is the quantity of wine in ml in that glass.</p>

<p>We recommend outputting y to 7 decimal places, but it is not required. y will be considered correct if it is close enough to the correct number: within an absolute or relative error of 10<sup>-6</sup>. </p>

