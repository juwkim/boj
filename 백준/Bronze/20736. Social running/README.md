# [Bronze I] Social running - 20736 

[문제 링크](https://www.acmicpc.net/problem/20736) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구현(implementation)

### 문제 설명

<p>You and a few friends are running together once a week around Lund. You all agree that it is boring and also dangerous to run on your own rather than running with others. Therefore you and your friends decide to minimize the distance that anyone needs to run on their own.</p>

<p>You are $N$ friends, who live in $N$ different locations numbered $0$ through $N-1$. Everyone will run exactly one lap going through all the locations in cyclic order (if you live in location $i$, you run $i\rightarrow i+1\pmod{N}\rightarrow\ldots\rightarrow N-1\rightarrow 0\rightarrow\ldots\rightarrow i-1\pmod{N}\rightarrow i$. Someone starts the run, then everyone joins the run as the group comes, runs exactly one lap and stops when the group comes back to their house.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 150px; height: 153px;"></p>

<p>Given that an optimal person starts the run, what is the minimal total distance that anyone has to run on their own? In the above example, an optimal choice would be to start the run at location $3$. Then the first runner has to run the leg from 3 to 0 alone, and it is easily checked that your friend living in location 2 also will be running alone from 1 to 2, for a total solitary distance of $4$.</p>

### 입력 

 <p>The first line of the input contains the number of friends in the group, $N$ ($2\leq N\leq 10$). It is followed by $N$ lines where the $i$-th line contains a single integer, the distance from location $i$ to location $i+1\pmod{N}$. Each distance is between $1$ and $10^4$.</p>

### 출력 

 <p>The output consists of a single integer, the minimal total distance anyone has to run on their own, given that the optimal person starts the run.</p>

