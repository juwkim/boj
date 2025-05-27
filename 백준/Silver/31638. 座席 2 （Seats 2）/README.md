# [Silver I] 座席 2 (Seats 2) - 31638 

[문제 링크](https://www.acmicpc.net/problem/31638) 

### 성능 요약

메모리: 167596 KB, 시간: 1016 ms

### 분류

정렬

### 제출 일자

2025년 5월 27일 10:50:41

### 문제 설명

<p>JOI 国では，今年プログラミングの世界大会が開かれることとなった．大会には <var>N</var> 人の選手が参加予定であり，選手には <var>1</var> から <var>N</var> までの番号が付けられている．</p>

<p>各選手の出身国は <var>1</var> 以上 <var>10<sup>9</sup></var> 以下の整数の番号で表され，選手 <var>i</var> (<var>1 ≦ i ≦ N</var>) の出身国は国 <var>C<sub>i</sub></var> である．<var>N</var> 人の選手の出身国がすべて同じであることはない． また，各選手の座席は直線状に並んでおり，選手 <var>i</var> (<var>1 ≦ i ≦ N</var>) の座席は位置 <var>X<sub>i</sub></var> にある．選手 <var>i</var> (<var>1 ≦ i ≦ N</var>) と選手 <var>j</var> (<var>1 ≦ j ≦ N</var>) の<strong>座席の距離</strong>は <var>|X<sub>i</sub> - X<sub>j</sub>|</var> である．ただし，<var>|x|</var> は <var>x</var> の絶対値を表す．</p>

<p>各選手は大会中他の選手と交流をするにあたって，自分とは出身国の異なる選手のうち，自分と座席が最も近い選手までの座席の距離を知りたい．</p>

<p>各選手の出身国と座席の位置の情報が与えられたとき，各選手 <var>i</var> (<var>1 ≦ i ≦ N</var>) について，選手 <var>i</var> とは出身国の異なる選手のうち，選手 <var>i</var> との座席の距離が最も小さい選手までの座席の距離を出力するプログラムを作成せよ．</p>

### 입력 

 <p>入力は以下の形式で与えられる．</p>

<pre><var>N</var>
<var>C<sub>1</sub></var>   <var>X<sub>1</sub></var>
<var>C<sub>2</sub></var>   <var>X<sub>2</sub></var>
<var>︙</var>
<var>C<sub>N</sub></var>   <var>X<sub>N</sub></var></pre>

### 출력 

 <p><var>N</var> 行出力せよ．<var>i</var> 行目 (<var>1 ≦ i ≦ N</var>) には，選手 <var>i</var> とは出身国の異なる選手のうち，選手 <var>i</var> との座席の距離が最も小さい選手までの座席の距離を出力せよ．</p>

