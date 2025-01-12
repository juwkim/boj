# [Bronze III] マスキングテープ (Masking Tape) - 33173 

[문제 링크](https://www.acmicpc.net/problem/33173) 

### 성능 요약

메모리: 116236 KB, 시간: 336 ms

### 분류

구현

### 제출 일자

2025년 1월 13일 07:37:22

### 문제 설명

<p>JOI 君は，紙とマスキングテープを使い，色塗りをして遊んでいる．</p>

<p>紙は長方形であり，縦 <var>H</var> 行，横 <var>W</var> 列のマス目が描かれている．上から <var>i</var> 行目 (<var>1 ≦ i ≦ H</var>)，左から <var>j</var> 列目 (<var>1 ≦ j ≦ W</var>) のマスをマス <var>(i, j)</var> と呼ぶ．</p>

<p>それぞれのマスには色が <var>1</var> つ定められている．色は整数で表され，はじめすべてのマスの色は <var>0</var> である．</p>

<p>JOI 君は，この紙とマスキングテープを用いて <var>Q</var> 回の操作を行う． <var>k</var> 回目 (<var>1 ≦ k ≦ Q</var>) の操作は，整数 <var>q<sub>k</sub></var> の値に応じて以下のように説明される．</p>

<ul>
	<li><var>q<sub>k</sub> = 1</var> のとき，この操作は整数 <var>x<sub>k</sub>, y<sub>k</sub>, c<sub>k</sub></var> で表される．マス <var>(x<sub>k</sub>, y<sub>k</sub>)</var>, <var>(x<sub>k</sub> + 1, y<sub>k</sub>)</var>, <var>(x<sub>k</sub>, y<sub>k</sub> + 1)</var>, <var>(x<sub>k</sub> + 1, y<sub>k</sub> + 1)</var> それぞれについて，マスがマスキングテープで覆われていなければ，そのマスの色を <var>c<sub>k</sub></var> に変更する．マスがマスキングテープで覆われているならば，そのマスには何もしない．</li>
	<li><var>q<sub>k</sub> = 2</var> のとき，この操作は整数 <var>x<sub>k</sub>, y<sub>k</sub></var> で表される．マス <var>(x<sub>k</sub>, y<sub>k</sub>)</var>, <var>(x<sub>k</sub> + 1, y<sub>k</sub>)</var>, <var>(x<sub>k</sub>, y<sub>k</sub> + 1)</var>, <var>(x<sub>k</sub> + 1, y<sub>k</sub> + 1)</var> をマスキングテープで覆う．</li>
</ul>

<p><var>Q</var> 回の操作が終わった後，すべてのマスキングテープを剥がす．なお，あるマスのマスキングテープを剥がしたとき，そのマスの色はマスキングテープで覆われる直前の色と同じになる．</p>

<p><var>Q</var> 回の操作の情報が与えられたとき，最終的な紙のすべてのマスの色を求めるプログラムを作成せよ．</p>

### 입력 

 <p>入力は以下の形式で与えられる．</p>

<pre><var>H</var> <var>W</var> <var>Q</var>
(<var>Query 1</var>)
(<var>Query 2</var>)
<var>:</var>
(<var>Query Q</var>)</pre>

<p>各 (<var>Query k</var>) (<var>1 ≦ k ≦ Q</var>) にはいくつかの整数が空白区切りで書かれている．そのうち <var>1</var> 個目の整数が <var>q<sub>k</sub></var> であり，この行の内容は以下のいずれかである．</p>

<ul>
	<li><var>q<sub>k</sub> = 1</var> のとき，この行には続いて <var>3</var> 個の整数 <var>x<sub>k</sub>, y<sub>k</sub>, c<sub>k</sub></var> が空白区切りで書かれている．</li>
	<li><var>q<sub>k</sub> = 2</var> のとき，この行には続いて <var>2</var> 個の整数 <var>x<sub>k</sub>, y<sub>k</sub></var> が空白区切りで書かれている．</li>
</ul>

### 출력 

 <p>最終的な紙のすべてのマスの色を <var>H</var> 行で出力せよ．<var>i</var> 行目 (<var>1 ≦ i ≦ H</var>) には，<var>W</var> 個の整数を空白区切りで出力せよ．ここで，<var>j</var> 番目 (<var>1 ≦ j ≦ W</var>) に出力する整数はマス <var>(i, j)</var> の色とする．</p>

