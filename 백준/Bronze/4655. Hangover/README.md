# [Bronze III] Hangover - 4655 

[문제 링크](https://www.acmicpc.net/problem/4655) 

### 성능 요약

메모리: 28776 KB, 시간: 112 ms

### 분류

수학(math)

### 문제 설명

<p>How far can you make a stack of cards overhang a table? If you have one card, you can create a maximum overhang of half a card length. (We're assuming that the cards must be perpendicular to the table.) With two cards you can make the top card overhang the bottom one by half a card length, and the bottom one overhang the table by a third of a card length, for a total maximum overhang of 1/2 <code>+</code> 1/3 <code>=</code> 5/6 card lengths. In general you can make <em>n</em> cards overhang by 1/2 <code>+</code> 1/3 <code>+</code> 1/4 <code>+</code> ... <code>+</code> 1/(<em>n</em> <code>+</code> 1) card lengths, where the top card overhangs the second by 1/2, the second overhangs tha third by 1/3, the third overhangs the fourth by 1/4, etc., and the bottom card overhangs the table by 1/(<em>n</em> <code>+</code> 1). This is illustrated in the figure below.</p>

<p style="text-align: center;"><img alt="" src="" style="height:115px; width:424px"></p>

### 입력 

 <p>The input consists of one or more test cases, followed by a line containing the number 0.00 that signals the end of the input. Each test case is a single line containing a positive floating-point number <em>c</em> whose value is at least 0.01 and at most 5.20; <em>c</em> will contain exactly three digits.</p>

### 출력 

 <p>For each test case, output the minimum number of cards necessary to achieve an overhang of at least <em>c</em> card lengths. Use the exact output format shown in the examples.</p>

