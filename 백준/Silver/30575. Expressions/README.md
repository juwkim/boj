# [Silver III] Expressions - 30575 

[문제 링크](https://www.acmicpc.net/problem/30575) 

### 성능 요약

메모리: 144672 KB, 시간: 328 ms

### 분류

구현, 수학

### 제출 일자

2024년 9월 14일 15:21:04

### 문제 설명

<p>Part of the training in arithmetic classes in Tomorrow Programming School consists of quick evaluation of a given arithmetic expression, in the head only. Fortunately, the expressions contain only positive integers, no brackets, and only three operations: addition, subtraction, and multiplication. Thus, the result is guaranteed to be an integer. Moreover, at introductory stages, a student has to evaluate only the parity of the result – is it odd or even?</p>

<p>Unfortunately, the professor presenting the expressions on the blackboard is known to be quite absentminded. He often rewrites various numbers in an expression, even more times, while the students are already calculating. Typically, it changes the value of the whole expression, and the students have to start their calculations all over again.</p>

<p>The students decided to write a program which would help them. The input of the program will be the original expression, and the sequence of subsequent value changes in it. For each change, the program will calculate the value of the modified expression, possibly even without recalculating the whole expression from scratch.</p>

### 입력 

 <p>The first input line contains two numbers N and M (1 ≤ N, M ≤ 10<sup>5</sup>), the number of integers in the expression, and the number of subsequent value changes in the expression. The second input line contains N token-separated integers A<sub>1</sub>, . . . , A<sub>N</sub> (1 ≤ A<sub>i</sub> ≤ 10<sup>9</sup>). Each token is +, -, or * (plus, minus, star (multiplication)). Each of the next M lines describe one value change in the expression. It contains two space-separated numbers X (1 ≤ X ≤ N) and Y (1 ≤ Y ≤ 10<sup>9</sup>), which means that the X-th number in the expression was changed to value Y.</p>

<p>The changes are considered to be subsequent, i.e., when a next change appears on a different position, the previous change in the expression is preserved.</p>

### 출력 

 <p>Output M + 1 lines. The i-th line contains either “even” or “odd”, depending on whether the input expression evaluates to an even or to an odd value after application of the first i − 1 changes. In particular, the first output line indicates whether the expression evaluates to an even or to an odd value before any change was done. The evaluation follows standard arithmetic rule of operations precedence. Multiplication is granted higher precedence than addition and subtraction.</p>

