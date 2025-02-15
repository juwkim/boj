# [Silver II] Matsuzaki Number - 22609 

[문제 링크](https://www.acmicpc.net/problem/22609) 

### 성능 요약

메모리: 111572 KB, 시간: 148 ms

### 분류

구현, 수학, 정수론, 소수 판정, 에라토스테네스의 체, 정렬

### 제출 일자

2025년 1월 8일 08:42:35

### 문제 설명

<p>Matsuzaki 教授は，宇宙の真理を研究している科学者である．人生，宇宙，すべての答えは 42 であると言われているが，Matsuzaki 教授はこれだけでは宇宙の真理を解明するには不十分であると考えている．Matsuzaki 教授は，宇宙の真理は 2 つのパラメータからなる関数で表されると考えており，42 はその 1 つに過ぎないというのである．</p>

<p>Matsuzaki 教授の定義した関数 M(<i>N</i>, <i>P</i>) は，<i>N</i> より大きい素数を 2 つ選んで（同じ数を 2 つでも構わない）和をとることで得られる数の全体を，小さいほうから順番に並べたときに，<i>P</i> 番目に現れる数を表す．ここで，2 通り以上の和で表されるような数も存在するが，そういった数は和の組み合わせの数と同じ個数だけ並べられる．</p>

<p>例として <i>N</i> = 0 の場合を考えよう．このときは素数全体から 2 つを選んで和をとることになる．そういった和のうちで最小の数を考えると，同じ数を 2 回選ぶことも許されていることから，2 + 2 = 4 であることがわかる．すなわち M(0, 1) = 4 である．次に小さい数は 2 + 3 = 5 であるから M(0, 2) = 5 となる．同様にして考えると，和を並べたものは 4, 5, 6, 7, 8, 9, 10, 10, 12, 13, 14, 14, 16, ... のようになることがわかる．すなわち，たとえば M(0, 9) = 12 である．</p>

<p>同じようにして <i>N</i> = 10 の場合を考えると，このときは 10 より大きい素数 {11, 13, 17, 19, ...} から 2 つを選ぶことになり，得られる和を小さいほうから並べると 22, 24, 26, 28, 30, 30, 32, ... のようになる．</p>

<p>あなたの仕事は，<i>N</i> と <i>P</i> が与えられた時に M(<i>N</i>, <i>P</i>) を計算するプログラムを書くことである．</p>

### 입력 

 <p>入力は複数のデータセットからなる．データセットは 1 行であり，2 つの整数 <i>N</i> (0 ≤ <i>N</i> ≤ 100,000) と <i>P</i> (1 ≤ <i>P</i> ≤ 100) が 1 つの空白で区切られて与えられる．</p>

<p>入力の終わりは，空白で区切られた 2 つの -1 を含む 1 行で示される．</p>

### 출력 

 <p>各データセットに対して，M(<i>N</i>, <i>P</i>) の値を 1 行に出力せよ．出力に余計な空白や改行を含めてはならない．</p>

