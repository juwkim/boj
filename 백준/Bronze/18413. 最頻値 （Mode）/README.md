# [Bronze II] 最頻値 (Mode) - 18413 

[문제 링크](https://www.acmicpc.net/problem/18413) 

### 성능 요약

메모리: 31996 KB, 시간: 84 ms

### 분류

구현(implementation)

### 문제 설명

<p>長さ <var>N</var> の数列 <var>A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub></var> が与えられる． この数列の各項は <var>1</var> 以上 <var>M</var> 以下の整数である．</p>

<p>長さ <var>M</var> の新たな数列 <var>B<sub>1</sub>, B<sub>2</sub>, ..., B<sub>M</sub></var> を以下のように定義する．</p>

<ul>
	<li>各 <var>j</var> (<var>1 ≦ j ≦ M</var>) に対して，<var>B<sub>j</sub></var> の値は <var>A<sub>i</sub> = j</var> を満たす整数 <var>i</var> (<var>1 ≦ i ≦ N</var>) の個数に等しい．</li>
</ul>

<p><var>B<sub>1</sub>, B<sub>2</sub>, ..., B<sub>M</sub></var> の最大値を求めよ．</p>

### 입력 

 <p>入力は以下の形式で標準入力から与えられる．</p>

<pre><var>N</var> <var>M</var>
<var>A<sub>1</sub></var> <var>A<sub>2</sub></var> <var>…</var> <var>A<sub>N</sub></var></pre>

### 출력 

 <p><var>B<sub>1</sub>, B<sub>2</sub>, ..., B<sub>M</sub></var> の最大値を <var>1</var> 行で出力せよ．</p>

