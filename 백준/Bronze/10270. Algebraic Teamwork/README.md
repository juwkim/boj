# [Bronze II] Algebraic Teamwork - 10270 

[문제 링크](https://www.acmicpc.net/problem/10270) 

### 성능 요약

메모리: 225416 KB, 시간: 7924 ms

### 분류

조합론(combinatorics), 수학(math)

### 문제 설명

<p>The great pioneers of group theory and linear algebra want to cooperate and join their theories. In group theory, permutations – also known as bijective functions – play an important role. For a finite set A, a function σ : A → A is called a permutation of A if and only if there is some function ρ : A → A with</p>

<p style="text-align: center;">σ(ρ(a)) = a and ρ(σ(a)) = a for all a ∈ A.</p>

<p>The other half of the new team – the experts on linear algebra – deal a lot with idempotent functions. They appear as projections when computing shadows in 3D games or as closure operators like the transitive closure, just to name a few examples. A function p : A → A is called idempotent if and only if</p>

<p style="text-align: center;">p(p(a)) = p(a) for all a ∈ A.</p>

<p>To continue with their joined research, they need your help. The team is interested in non-idempotent permutations of a given finite set A. As a first step, they discovered that the result only depends on the set’s size. For a concrete size 1 ≤ n ≤ 10<sup>5</sup>, they want you to compute the number of permutations on a set of cardinality n that are not idempotent.</p>

### 입력 

 <p>The input starts with the number t ≤ 100 of test cases. Then t lines follow, each containing the set’s size 1 ≤ n ≤ 10<sup>5</sup>.</p>

### 출력 

 <p>Output one line for every test case containing the number modulo 1 000 000 007 = (10<sup>9</sup> + 7) of non-idempotent permutations on a set of cardinality n.</p>

