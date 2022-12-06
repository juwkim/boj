# [Bronze II] 幹線道路 (Trunk Road) - 15476 

[문제 링크](https://www.acmicpc.net/problem/15476) 

### 성능 요약

메모리: 29200 KB, 시간: 220 ms

### 분류

브루트포스 알고리즘(bruteforcing)

### 문제 설명

<p>JOI 市は，東西方向にまっすぐに伸びる <var>H</var> 本の道路と，南北方向にまっすぐに伸びる <var>W</var> 本の道路によって，碁盤の目の形に区分けされている．道路と道路の間隔は <var>1</var> である．JOI 市では，これら <var>H+W</var> 本の道路から，東西方向に <var>1</var> 本，南北方向に <var>1</var> 本，合計 <var>2</var> 本の道路を幹線道路として選ぶことになった．</p>

<p>北から <var>i</var> 本目 (<var>1≦i≦H</var>) の道路と，西から <var>j</var> 本目 (<var>1≦j≦W</var>) の道路の交差点を，交差点 <var>(i,j)</var> とする．交差点 <var>(i,j)</var> と北から <var>m</var> 本目 (<var>1≦m≦H</var>) の道路の距離は <var>|i-m|</var> であり，交差点 <var>(i,j)</var> と西から <var>n</var> 本目 (<var>1≦n≦W</var>) の道路の距離は <var>|j-n|</var> である． また，交差点 <var>(i,j)</var> の近くには <var>A_{i,j}</var> 人の住人が住んでいる．</p>

<p><var>2</var> 本の幹線道路を選んだときの，JOI 市の全ての住人に対する，最寄りの交差点から近い方の幹線道路への距離の総和の最小値を求めよ．</p>

### 입력 

 <p>入力は以下の形式で標準入力から与えられる．</p>

<pre><var>H</var> <var>W</var>
<var>A_{1,1}</var> <var>A_{1,2}</var> ... <var>A_{1,W}</var>
:
<var>A_{H,1}</var> <var>A_{H,2}</var> ... <var>A_{H,W}</var>
</pre>

### 출력 

 <p>JOI 市の全ての住人に対する，最寄りの交差点から近い方の幹線道路への距離の総和の最小値を出力せよ．</p>

