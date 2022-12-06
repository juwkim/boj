# [Bronze II] Methodic Multiplication - 21059 

[문제 링크](https://www.acmicpc.net/problem/21059) 

### 성능 요약

메모리: 29428 KB, 시간: 64 ms

### 분류

파싱(parsing), 문자열(string)

### 문제 설명

<p>After one computer crash too many, Alonso has had enough of all this shoddy software and poorly written code!  He decides that in order for this situation to improve, the glass house that is modern programming needs to be torn down and rebuilt from scratch using only completely formal axiomatic reasoning.  As one of the first steps, he decides to implement arithmetic with natural numbers using the Peano axioms.</p>

<p>The Peano axioms (named after Italian mathematican Giuseppe Peano) are an axiomatic formalization of the arithmetic properties of the natural numbers.  We have two symbols: the constant $0$, and a unary successor function $S$.  The natural numbers, starting at $0$, are then $0$, $S(0)$, $S(S(0))$, $S(S(S(0)))$, and so on.  With these two symbols, the operations of <em>addition</em> and <em>multiplication</em> are defined inductively by the following axioms: for any natural numbers $x$ and $y$, we have \[ \begin{align*} x + 0 &= x            &    x \cdot 0 &= 0 \\ x + S(y) &= S(x + y)  &    x \cdot S(y) &= x \cdot y + x \end{align*} \] The two axioms on the left define addition, and the two on the right define multiplication.</p>

<p>For instance, given $x = S(S(0))$ and $y = S(0)$ we can repeatedly apply these axioms to derive \[ \begin{align*} x \cdot y &= S(S(0)) \cdot S(0) = S(S(0)) \cdot 0 + S(S(0))\\ &= 0 + S(S(0)) = S(0 + S(0)) = S(S(0 + 0)) = S(S(0)) \end{align*}\] Write a program which given two natural numbers $x$ and $y$, defined in Peano arithmetic, computes the product $x \cdot y$.</p>

### 입력 

 <p>The input consists of two lines. Each line contains a natural number defined in Peano arithmatic, using at most $1\,000$ characters.</p>

### 출력 

 <p>Output the product of the two input numbers.</p>

