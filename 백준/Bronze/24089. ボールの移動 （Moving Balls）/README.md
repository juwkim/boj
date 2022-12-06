# [Bronze II] ボールの移動 (Moving Balls) - 24089 

[문제 링크](https://www.acmicpc.net/problem/24089) 

### 성능 요약

메모리: 30840 KB, 시간: 148 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p><var>N</var> 個のボールがあり，<var>1</var> から <var>N</var> までの番号が付けられている．また，何個でもボールを入れることのできる <var>N</var> 個の箱があり，箱には <var>1</var> から <var>N</var> までの番号が付けられている．</p>

<p>箱 <var>i</var> (<var>1 ≦ i ≦ N</var>) には最初，ボール <var>i</var> が入っていた．</p>

<p>JOI 高校の生徒である葵は，この状態から箱とボールに対して <var>M</var> 回の操作を行った．<var>j</var> 回目 (<var>1 ≦ j ≦ M</var>) の操作は，次のように行われた．</p>

<ul>
	<li>ボール <var>X<sub>j</sub></var> が入っている箱を探し，その箱からボール <var>X<sub>j</sub></var> を取り出す．その後，箱 <var>Y<sub>j</sub></var> にボール <var>X<sub>j</sub></var> を入れる．</li>
</ul>

<p>葵が <var>M</var> 回の操作をすべて終えた後，<var>N</var> 個のボールがそれぞれどの箱に入っているかを求めよ．</p>

### 입력 

 <p>入力は以下の形式で標準入力から与えられる．</p>

<pre><var>N</var> <var>M</var>
<var>X<sub>1</sub></var> <var>Y<sub>1</sub></var>
<var>X<sub>2</sub></var> <var>Y<sub>2</sub></var>
<var>:</var>
<var>X<sub>M</sub></var> <var>Y<sub>M</sub></var></pre>

### 출력 

 <p><var>N</var> 行で出力せよ．<var>i</var> 行目 (<var>1 ≦ i ≦ N</var>) には，葵が <var>M</var> 回の操作をすべて終えた後，ボール <var>i</var> が入っている箱の番号を出力せよ．</p>

