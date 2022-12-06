# [Bronze II] 運動会 (Sports Day) - 24088 

[문제 링크](https://www.acmicpc.net/problem/24088) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>JOI 高校には <var>N</var> 人の生徒がおり，<var>1</var> から <var>N</var> までの出席番号が付けられている．</p>

<p>来月 JOI 高校では運動会が開催され，<var>N</var> 人の生徒全員がこれに参加する．生徒のうち <var>K</var> 人が赤組に，残りの <var>N-K</var> 人が白組に属している．</p>

<p>出席番号 <var>N</var> 番の葵は，自分がどちらの組に属しているかを忘れてしまった．そこで，自分以外の生徒 <var>N-1</var> 人それぞれがどちらの組に属しているかを聞いてまわることで，自分がどちらの組に属しているかを判断することにした．</p>

<p>葵以外の <var>N-1</var> 人の組み分けの情報は，長さ <var>N-1</var> の文字列 <var>S</var> で表される．<var>S</var> の各文字は <code>R</code>，<code>W</code> のいずれかであり，その意味は次の通りである．</p>

<ul>
	<li><var>S</var> の <var>i</var> 文字目 (<var>1 ≦ i ≦ N-1</var>) が <code>R</code> の場合は，出席番号 <var>i</var> 番の生徒が赤組に属していることを表す．</li>
	<li><var>S</var> の <var>i</var> 文字目 (<var>1 ≦ i ≦ N-1</var>) が <code>W</code> の場合は，出席番号 <var>i</var> 番の生徒が白組に属していることを表す．</li>
</ul>

<p>葵が赤組に属しているならば <code>R</code> と，白組に属しているならば <code>W</code> と出力せよ．</p>

### 입력 

 <p>入力は以下の形式で標準入力から与えられる．</p>

<pre><var>N</var>
<var>K</var>
<var>S</var></pre>

### 출력 

 <p>葵が赤組に属しているならば <code>R</code> と，白組に属しているならば <code>W</code> と出力せよ．</p>

