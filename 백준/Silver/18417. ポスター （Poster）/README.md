# [Silver IV] ポスター (Poster) - 18417 

[문제 링크](https://www.acmicpc.net/problem/18417) 

### 성능 요약

메모리: 150476 KB, 시간: 328 ms

### 분류

구현(implementation)

### 문제 설명

<p>JOI 君は文化祭でのクラスの出し物を宣伝するため，ポスターを作った．そのポスターは <var>N</var> 行 <var>N</var> 列のマス目の形をしており，各マスは赤，緑，青のいずれかの色で塗られている．ポスターの上から <var>i</var> 行目，左から <var>j</var> 列目 (<var>1 ≦ i ≦ N</var>，<var>1 ≦ j ≦ N</var>) にあるマスの色は，<var>S<sub>i,j</sub>=</var> `R' のとき赤色，<var>S<sub>i,j</sub>=</var> `G' のとき緑色，<var>S<sub>i,j</sub>=</var> `B' のとき青色である．</p>

<p>しかし，このポスターにクラスのみんなは満足してはくれなかった．話し合いの結果，マス目の形は変えずに色の配置を変えることで，新しいポスターを作ることに決まった．新しいポスターの上から <var>i</var> 行目，左から <var>j</var> 列目 (<var>1 ≦ i ≦ N</var>，<var>1 ≦ j ≦ N</var>) にあるマスの色は，<var>T<sub>i,j</sub>=</var> `R' のとき赤色，<var>T<sub>i,j</sub>=</var> `G' のとき緑色，<var><sub>i,j</sub>=</var> `B' のとき青色となるようにする．</p>

<p>JOI 君は今あるポスターに以下のいずれかの作業を繰り返し行うことで，新しいポスターを作ることにした．</p>

<ul>
	<li>マスを一つ選び，そのマスの色を好きな色に塗りなおす．</li>
	<li>ポスター全体を <var>90°</var> 時計回りに回転させる．このとき，もともと上から <var>i</var> 行目，左から <var>j</var> 列目 (<var>1 ≦ i ≦ N</var>，<var>1 ≦ j ≦ N</var>) にあるマスは，上から <var>j</var> 行目，左から <var>N-i+1</var> 列目にあるマスに移動する．</li>
	<li>ポスター全体を <var>90°</var> 反時計回りに回転させる．このとき，もともと上から <var>i</var> 行目，左から <var>j</var> 列目 (<var>1 ≦ i ≦ N</var>，<var>1 ≦ j ≦ N</var>) にあるマスは，上から <var>N-j+1</var> 行目，左から <var>i</var> 列目にあるマスに移動する．</li>
</ul>

<p>JOI 君はどの作業をするにも <var>1</var> 分かかる．JOI 君が作ったポスター，新しく作るポスターの情報が与えられたとき，JOI 君が新しいポスターを作るのに最短で何分かかるかを求めるプログラムを作成せよ．</p>

### 입력 

 <p>入力は以下の形式で標準入力から与えられる．</p>

<pre><var>N</var>
<var>S<sub>1,1</sub> … S<sub>1,N</sub></var>
<var>:</var>
<var>S<sub>N,1</sub> … S<sub>N,N</sub></var>
<var>T<sub>1,1</sub> … T<sub>1,N</sub></var>
<var>:</var>
<var>T<sub>N,1</sub> … T<sub>N,N</sub></var></pre>

### 출력 

 <p>新しいポスターを作るのに最短で何分かかるかを <var>1</var> 行で出力せよ．</p>

