# [Silver III] 鐘 (Bell) - 27543 

[문제 링크](https://www.acmicpc.net/problem/27543) 

### 성능 요약

메모리: 180844 KB, 시간: 440 ms

### 분류

이분 탐색

### 제출 일자

2024년 2월 14일 06:02:16

### 문제 설명

<p>JOI 市には <var>1</var> 本の十分に長い道路がある．この道路は数直線とみなすことができ，各地点は <var>1</var> 個の実数による座標で表される．</p>

<p>また，JOI 市にはこの道路に沿って <var>N</var> 個の鐘があり，座標の小さい順に <var>1</var> から <var>N</var> までの番号が付けられている．鐘 <var>i</var> (<var>1 ≦ i ≦ N</var>) は座標 <var>A<sub>i</sub></var> にある．</p>

<p>JOI 市では，<var>1</var> 年の終わりにこれらの鐘を一斉に鳴らすのが一大イベントとなっている．</p>

<p>どの鐘も，鳴らすとその鐘と同じ地点では強さ <var>K</var> の音で聞こえるが，距離が <var>1</var> 離れるごとに聞こえる音の強さは <var>1</var> 小さくなり，距離が <var>K</var> 以上離れると <var>0</var> になる．すなわち，鐘 <var>i</var> を鳴らしたとき，座標 <var>x</var> で聞こえる鐘 <var>i</var> の音の強さは <var>max{ K - |x - A<sub>i</sub>|, 0 }</var> である．ただし，<var>|t|</var> は <var>t</var> の絶対値を表す．</p>

<p>すべての鐘を鳴らしたとき，座標 <var>x</var> で聞こえる鐘の音の強さは，座標 <var>x</var> で聞こえるそれぞれの鐘の音の強さの最大値である．</p>

<p>JOI 市にはこの道路に沿って <var>M</var> 個の家があり，古い方から順に <var>1</var> から <var>M</var> までの番号が付けられている．家 <var>j</var> (<var>1 ≦ j ≦ M</var>) は座標 <var>B<sub>j</sub></var> にある．</p>

<p>JOI 市の市長であるあなたは，すべての鐘を鳴らしたとき，それぞれの家で聞こえる鐘の音の強さを知りたい．</p>

<p>JOI 市の鐘と家の情報が与えられたとき，すべての鐘を鳴らしたときに座標 <var>B<sub>1</sub>, B<sub>2</sub>, …, B<sub>M</sub></var> で聞こえる鐘の音の強さを求めるプログラムを作成せよ．</p>

### 입력 

 <p>入力は以下の形式で与えられる．</p>

<pre><var>N</var> <var>M</var> <var>K</var>
<var>A<sub>1</sub></var> <var>A<sub>2</sub></var> <var>…</var> <var>A<sub>N</sub></var>
<var>B<sub>1</sub></var> <var>B<sub>2</sub></var> <var>…</var> <var>B<sub>M</sub></var></pre>

### 출력 

 <p><var>M</var> 行出力せよ．<var>j</var> 行目 (<var>1 ≦ j ≦ M</var>) には，すべての鐘を鳴らしたときに座標 <var>B<sub>j</sub></var> で聞こえる鐘の音の強さを出力せよ．</p>

