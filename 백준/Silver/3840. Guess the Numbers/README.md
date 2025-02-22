# [Silver II] Guess the Numbers - 3840 

[문제 링크](https://www.acmicpc.net/problem/3840) 

### 성능 요약

메모리: 169412 KB, 시간: 3936 ms

### 분류

브루트포스 알고리즘, 파싱, 문자열

### 제출 일자

2025년 2월 22일 13:52:19

### 문제 설명

<p>John has never been very good at maths. Due to his bad grades, his parents have sent him to the Academic Coalition of Mathematics (ACM). Despite the large amount of money his parents are spending on the ACM, John does not pay much attention during classes. However, today he has begun to think about all the effort his parents are putting into his education, and he has started to feel somewhat. . . guilty. So he has made a decision: he is going to improve his maths grades!</p>

<p>However, no sooner had he resolved to pay attention than the lesson ended. So the only thing he has been able to do is to hurriedly copy the content of the blackboard in his notebook. Today, the teacher was explaining basic arithmetic expressions with unknowns. He vaguely remembers that his classmates have been substituting values into the unknowns to obtain the expressions’ results. However, in all the hurry, John has only written down expressions, values and results in a messy fashion. So he does not know which value comes with each unknown, or which result goes with each expression.</p>

<p>That is the reason he needs your help: he wants to know, given an expression, some values and a result, whether it is possible or not to assign those values to the unknowns in order for the expression to evaluate to the given result. The particular assignment of values does not matter to John, as he wants to do it by himself. He only wants to know whether it is possible or not.</p>

### 입력 

 <p>Each test case in the input file consists of two lines:</p>

<ul>
	<li>The first line contains a sequence of natural numbers. The first one (1 ≤ n ≤ 5) is the number of unknowns that will occur in the expression. It is followed by a sequence of n integers v1 . . . vn (0 ≤ vi ≤ 50), which are the values to be assigned to the unknowns. Finally, there is an integer m (0 ≤ m ≤ 1000) representing the desired result of the evaluation of the expression.</li>
	<li>The second line contains an arithmetic expression composed of lowercase letters (a-z), brackets (( and )) and binary operators (+, -, *). This expression will contain n unknowns, represented by n different lowercase letters, without repetitions. The expression will not contain any blanks and will always be syntactically correct, i.e. it is just an unknown or has the form (e1 op e2 ), where e1 and e2 are expressions and op is one of the three possible binary operators.</li>
</ul>

<p>The input will finish with a dummy test case of just one line containing 0 0, which must not be processed.</p>

### 출력 

 <p>For each test case, print a single line with YES if there exists an assignment of the values v1 . . . vn to the unknowns such that the expression evaluates to m, and NO otherwise. Notice that each value vi must be assigned to exactly one unknown.</p>

