# [Bronze II] 箱と鍵 (Boxes and Keys) - 24081 

[문제 링크](https://www.acmicpc.net/problem/24081) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>ビーバーのビ太郎は，鍵のかかった <var>N</var> 個の宝箱と <var>M</var> 個の鍵を手に入れた．<var>N</var> 個の宝箱には <var>1</var> から <var>N</var> までの番号が付けられており，宝箱 <var>i</var> (<var>1 ≦ i ≦ N</var>) には整数 <var>A<sub>i</sub></var> が書かれている．<var>M</var> 個の鍵には <var>1</var> から <var>M</var> までの番号が付けられており，鍵 <var>j</var> (<var>1 ≦ j ≦ M</var>) には整数 <var>B<sub>j</sub></var> が書かれている．</p>

<p>宝箱 <var>i</var> は整数 <var>A<sub>i</sub></var> が書かれた鍵を使うことで解錠できる．同じ鍵を使って複数の宝箱を解錠してもよい．</p>

<p>ビ太郎は，できるだけ多くの宝箱を解錠したい．ビ太郎が解錠できる宝箱の個数の最大値を求めよ．</p>

### 입력 

 <p>入力は以下の形式で標準入力から与えられる．</p>

<pre><var>N</var> <var>M</var>
<var>A<sub>1</sub></var> <var>A<sub>2</sub></var> … <var>A<sub>N</sub></var>
<var>B<sub>1</sub></var> <var>B<sub>2</sub></var> … <var>B<sub>M</sub></var></pre>

### 출력 

 <p>ビ太郎が解錠できる宝箱の個数の最大値を出力せよ．</p>

