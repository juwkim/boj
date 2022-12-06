# [Silver V] Musical Trees - 24822 

[문제 링크](https://www.acmicpc.net/problem/24822) 

### 성능 요약

메모리: 113248 KB, 시간: 116 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>It's Christmas time and JW's 1-dimensional shop is selling Christmas trees. However, the demand for trees is much higher than the number of trees available. Hence, JW has come up with a special strategy to help decide who gets what tree: a game of Musical Trees!</p>

<p>Musical Trees is much like the game Musical Chairs. There's a set of trees lined up in a straight (1-dimensional) line. At first, everyone starts by wandering around the store while the music is playing. When the music stops, everyone runs to the nearest tree (the tree the smallest distance away) and whoever reaches a tree first gets to the claim that tree. Since people are lazy, they will only ever try to run to the closest tree to them, and hence multiple people may try to get the same tree. Note this means some trees may be unclaimed if they are closest to no one. Also, like in Musical Chairs, no tree can be claimed by more than one person.</p>

<p>The music has just stopped in Musical Trees and as everyone is running to the closest tree, you want to figure out the number of people who won't get any tree.</p>

### 입력 

 <p>The first line consists the number of people $n$ ($1\le n\le 100$) and the number of trees $m$ ($1 \le m \le 100$). The next line contains $n$ integers $p_1,p_2,\ldots,p_n$, the position of all the people when the music stops ($1 \le p_i \le 1\,000$). The last line contains $m$ integers $t_1,t_2,\ldots,t_m$, the position of all the trees ($1 \le t_i \le 1\,000$). No two people or two trees will have the same position. Some people may try to cheat though, and will already be at the same position as a tree when the music stops. Note that if a person has more than one closest tree to them, they will always go for the one with the smallest $t_i$.</p>

### 출력 

 <p>Output the number of people who won't get a tree.</p>

