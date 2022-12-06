# [Bronze I] マージ (Merge) - 18410 

[문제 링크](https://www.acmicpc.net/problem/18410) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

구현(implementation), 정렬(sorting)

### 문제 설명

<p>長さ <var>N</var> の正整数列 <var>A=(A<sub>1</sub>, A<sub>2</sub>, ..., A<sub>N</sub>)</var> と，長さ <var>M</var> の正整数列 <var>B=(B<sub>1</sub>, B<sub>2</sub>, ..., B<sub>M</sub>)</var> が与えられる． これらの数列は，共に広義単調増加数列である．つまり，<var>A<sub>1</sub> ≦ A<sub>2</sub> ≦ … ≦ A<sub>N</sub></var>, <var>B<sub>1</sub> ≦ B<sub>2</sub> ≦ … ≦ B<sub>M</sub></var> を満たす．</p>

<p>以下のアルゴリズムを用いて，これらの数列から，長さ <var>N+M</var> の正整数列 <var>C=(C<sub>1</sub>, C<sub>2</sub>, ..., C<sub>N+M</sub>)</var> を生成する．</p>

<ol>
	<li>はじめ <var>C</var> は空とする．</li>
	<li><var>A</var> と <var>B</var> がどちらも空の場合，終了する．</li>
	<li><var>A</var> と <var>B</var> のどちらかが空の場合，そうでない数列を <var>t</var> とおく．どちらも空でない場合，先頭の要素が小さい数列を <var>t</var> とおく．ただし，<var>A</var> と <var>B</var> の先頭の要素が同じ値のときは <var>A</var> を <var>t</var> とおく．</li>
	<li><var>t</var> の先頭の要素を <var>C</var> の末尾に追加する．</li>
	<li><var>t</var> の先頭の要素を削除する．</li>
	<li>2. に戻る．</li>
</ol>

<p>広義単調増加な正整数列 <var>A</var>, <var>B</var> が与えられたとき，このアルゴリズムにより生成される正整数列 <var>C</var> を出力するプログラムを作成せよ．</p>

### 입력 

 <p>入力は以下の形式で標準入力から与えられる．</p>

<pre><var>N</var> <var>M</var>
<var>A<sub>1</sub></var> <var>A<sub>2</sub></var> <var>…</var> <var>A<sub>N</sub></var>
<var>B<sub>1</sub></var> <var>B<sub>2</sub></var> <var>…</var> <var>B<sub>M</sub></var></pre>

### 출력 

 <p>標準出力に <var>N + M</var> 行出力せよ．</p>

<p><var>k</var> 行目 (<var>1 ≦ k ≦ N + M</var>) には，<var>C<sub>k</sub></var> を出力せよ．</p>

