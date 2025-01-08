# [Silver II] Auxiliary Question of the Universe - 3550 

[문제 링크](https://www.acmicpc.net/problem/3550) 

### 성능 요약

메모리: 109412 KB, 시간: 92 ms

### 분류

애드 혹, 해 구성하기, 구현, 문자열

### 제출 일자

2025년 1월 8일 20:10:55

### 문제 설명

<p>As you probably know, scientists already discovered the Ultimate question of life, the Universe, and everything, and it is "What do you get if you multiply six by nine?". Not satisfied by this, the scientists contracted a small Magrateyan company to construct a mini-computer to find out some more specific question (they named it <em>auxiliary</em>), which can theoretically shed more light on life, the Universe or something else.</p>

<p>This computer was built, but unluckily (although not unexpectedly) the result of computation was corrupted and partially lost. Finally the computer constructors managed to receive a string, which is a part of the correct question. After thorough analysis the constructors started to believe that the original result can be reconstructed from the string by adding some letters to it without the string letters being reordered or removed. Also they believe that the correct result is an arithmetic expression (as with the Ultimate question), but since the question is auxiliary, it contains no multiplication, only addition. More precisely, it should correspond to the following grammar:</p>

<pre><expression> ::= <term> | <term> <code>+</code> <expression>
<term> ::= <number> | <code>(</code> <expression> <code>)
</code><number> ::= <code>0</code> ... <code>9</code> [ <number> ]</pre>

<p>The constructors do not want to risk again, and they need your help to give just something to their clients. They ask you to reconstruct the question based on the corrupted computer answer which they managed to retrieve. </p>

### 입력 

 <p>The input file contains exactly one line --- the corrupted auxiliary question. It is a non-empty string which is at most 1000 symbols long. This string contains only symbols <code>+</code>, <code>(</code>, <code>)</code>, and <code>0</code>, ..., <code>9</code>.</p>

### 출력 

 <p>Output the reconstructed auxiliary question. It's guaranteed that there exists a correct question of less than 5000 symbols and your solution must also be shorter than that. If there is more than one solution, output any one.</p>

