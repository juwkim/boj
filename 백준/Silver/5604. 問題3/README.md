# [Silver IV] 問題3 - 5604 

[문제 링크](https://www.acmicpc.net/problem/5604) 

### 성능 요약

메모리: 131932 KB, 시간: 652 ms

### 분류

백트래킹(backtracking), 깊이 우선 탐색(dfs), 그래프 이론(graphs), 그래프 탐색(graph_traversal), 구현(implementation), 재귀(recursion)

### 문제 설명

<p>同じ大きさの正方形の紙が n 枚ある．これらの紙の下部を水平に揃えて何列 かに並べる．ただし，隣り合う列は左側が右側より低くならないように並べなけれ ばならない．例えば, n = 5 のときは，次のような 7 通りの並べ方が可能である．</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/ec4ea868-fe5f-4f56-929b-d5e5643f090b/-/preview/" style="width: 405px; height: 87px;"></p>

<p>これらを，各列に並んだ正方形の個数の列で表すことにする．例えば，n = 5 の ときは，それぞれ，</p>

<p style="text-align: center;">(5) (4, 1) (3, 2) (3, 1, 1) (2, 2, 1) (2, 1, 1, 1) (1, 1, 1, 1, 1)</p>

<p>と表わされる．</p>

<p>n を入力したとき， 辞書式順序で全て出力するプログラムを作成せよ．n ≤ 30 とする．ただし, 辞書式順序とは２つの並べ方 (a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>s</sub>) が並べ方 (b<sub>1</sub>, b<sub>2</sub>, ..., b<sub>t</sub>) に対して, a<sub>1</sub> > b<sub>1</sub> または, ある整数 i > 1 が存在して a<sub>1</sub> = b<sub>1</sub>, ..., a<sub>i−1</sub> = b<sub>i−1</sub> かつ a<sub>i</sub> > b<sub>i</sub> が成り立つとき (a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>s</sub>) が (b<sub>1</sub>, b<sub>2</sub>, ..., b<sub>t</sub>) より先に出力されるように並 べることである.</p>

### 입력 

 <p>1 行からなり, 1 行目に n が書かれている．</p>

### 출력 

 <p>辞書式順序で1 行に１通りずつ書き最後に改行を入れること. 並べ方は (a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>s</sub>) の出力は整数 a<sub>1</sub>, a<sub>2</sub>, . . . , a<sub>s</sub> をこの順番に空白で区切って出力すること.</p>

