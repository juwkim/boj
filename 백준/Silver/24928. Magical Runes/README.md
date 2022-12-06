# [Silver V] Magical Runes - 24928 

[문제 링크](https://www.acmicpc.net/problem/24928) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

애드 혹(ad_hoc), 비트마스킹(bitmask), 구현(implementation), 수학(math), 문자열(string)

### 문제 설명

<p>You maintain a very nice collection of magical runes. They generally come in two types, type <code>A</code> and type <code>B</code>.</p>

<p>You have arranged your runes on a shelf to show them off. Because they are magical runes, they change each day. That is, at the start of each day the leftmost rune will switch its type (i.e. from <code>A</code> to <code>B</code> or from <code>B</code> to <code>A</code>, depending on its type just before the start of the day). Every other rune will only change if the type of the rune to its left changes from <code>B</code> to <code>A</code>.</p>

<p>For example, if you have three runes initially arranged like <code>ABBAA</code>, then at the start of the next day only the leftmost rune will change and the sequence will look like <code>BBBAA</code>. After another day, the leftmost rune will change, but then the second rune from the left will change because the rune beside it changed from <code>B</code> to <code>A</code>. But then the third rune will also change for the same reason. And then the fourth rune will also change! That is, after the changes at the start of this day the runes will look like <code>AAABA</code>.</p>

<p>Your task is the following. Given the initial states $S$ of an initial arrangement of runes and given a number of days 𝐷D, you should determine the states of the runes after $D$ days have elapsed.</p>

### 입력 

 <p>Input consists of a single line that first begins with a string $S$ followed by an integer $D$. The length of $S$ will be between $1$ and $30$ (inclusive) and $S$ will consist only of characters <code>A</code> and <code>B</code>. The value $D$ satisfies $0≤D<2^{30}$.</p>

<p>Finally, you are also guaranteed that the rightmost rune does not change from <code>B</code> to <code>A</code> at the start of any of the $D$ days that you are to consider.</p>

### 출력 

 <p>Display a single string showing the states of the runes after $D$ days have elapsed, given they started in state $S$.</p>

