# [Bronze I] Card Divisibility - 24924 

[문제 링크](https://www.acmicpc.net/problem/24924) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

수학(math), 정수론(number_theory)

### 문제 설명

<p>Since you have learned Modular Arithmetic, you know how to work with quotients and remainders. For every pair of integers $a$ and $m$ with $m>0$, there exist unique integers $q$ and $r$ such that $a=m⋅q+r$ and $0≤r<m$. But this is a bit simple, you wonder if you can do something more interesting with this theory.</p>

<p>Right now, you are holding a handful of consecutive cards numbered from $L$ to $R$. You lay the cards out side-by-side to create a single large number (i.e. concatenating the digits of your cards). You would like to know the remainder (which is the $r$ in $a=m⋅q+r$) when this number is divided by $9$. For example, $L=9$ and $R=11$ means you are holding cards $9,10,11$. Concatenating these numbers produces the number $91011$. The remainder $r$ left upon dividing this number by $9$ would be $r=3$.</p>

### 입력 

 <p>Input consists of a single line containing two integers $L$ ($1≤L≤10^{12}$) and $R$ ($L≤R≤10^{12}$). This means you are holding the cards with numbers from $L$ to $R$, inclusive.</p>

### 출력 

 <p>Display a single line containing the remainder of the concatenated number if you were to divide it by $9$.</p>

