# [Silver IV] Game of Throwns - 15088 

[문제 링크](https://www.acmicpc.net/problem/15088) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

자료 구조(data_structures), 구현(implementation), 파싱(parsing), 시뮬레이션(simulation), 스택(stack), 문자열(string)

### 문제 설명

<p>Daenerys frequently invents games to help teach her second grade Computer Science class about various aspects of the discipline. For this week’s lesson she has the children form a circle and (carefully) throw around a petrified dragon egg.</p>

<p>The n children are numbered from 0 to n − 1 (it is a Computer Science class after all) clockwise around the circle. Child 0 always starts with the egg. Daenerys will call out one of two things:</p>

<ol>
	<li>a number t, indicating that the egg is to be thrown to the child who is t positions clockwise from the current egg holder, wrapping around if necessary. If t is negative, then the throw is to the counterclockwise direction.</li>
	<li>the phrase undo m, indicating that the last m throws should be undone. Note that undo commands never undo other undo commands; they just undo commands described in item 1 above.</li>
</ol>

<p>For example, if there are 5 children, and the teacher calls out the four throw commands 8 -2 3 undo 2, the throws will start from child 0 to child 3, then from child 3 to child 1, then from child 1 to child 4. After this, the undo 2 instructions will result in the egg being thrown back from child 4 to child 1 and then from child 1 back to child 3. If Daenerys calls out 0 (or n, −n, 2n, −2n, etc.) then the child with the egg simply throws it straight up in the air and (carefully) catches it again.</p>

<p>Daenerys would like a little program that determines where the egg should end up if her commands are executed correctly. Don’t ask what happens to the children if this isn’t the case.</p>

### 입력 

 <p>Input consists of two lines. The first line contains two positive integers n k (1 ≤ n ≤ 30, 1 ≤ k ≤ 100) indicating the number of students and how many throw commands Daenerys calls out, respectively. The following line contains the k throw commands. Each command is either an integer p (−10 000 ≤ p ≤ 10 000) indicating how many positions to throw the egg clockwise or undo m (m ≥ 1) indicating that the last m throws should be undone. Daenerys never has the kids undo beyond the start of the game.</p>

### 출력 

 <p>Display the number of the child with the egg at the end of the game.</p>

