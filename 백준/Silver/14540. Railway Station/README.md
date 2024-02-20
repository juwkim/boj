# [Silver III] Railway Station - 14540 

[문제 링크](https://www.acmicpc.net/problem/14540) 

### 성능 요약

메모리: 111136 KB, 시간: 156 ms

### 분류

자료 구조, 스택

### 제출 일자

2024년 2월 21일 05:09:47

### 문제 설명

<p>There is a famous railway station in one hilly country. The station was built in many decades ago when funds were extremely limited at that time. It was possible to establish only a surface track. Moreover, it turned out that the station could be only a dead-end one (see picture) and due to lack of available space it could have only one track.</p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/14540/1.png" style="height:126px; width:233px"></p>

<p>The local tradition is that every train arriving from the direction <em>A</em> continues in the direction <em>B</em> with coaches reorganized in some way. Assume that the train arriving from the direction <em>A</em> has <em>N</em> ≤1000 coaches numbered in increasing order 1, 2, ..., <em>N</em>. The chief for train reorganizations must know whether it is possible to marshal coaches continuing in the direction <em>B</em> so that their order will be<em>a</em><sub>1</sub>, <em>a</em><sub>2</sub>, …, <em>a<sub>N</sub></em>.</p>

<p> Help him and write a program that decides whether it is possible to get the required order of coaches. You can assume that single coaches can be disconnected from the train before they enter the station and that they can move themselves until they are on the track in the direction <em>B</em>. You can also suppose that at any time there can be located as many coaches as necessary in the station. But once a coach has entered the station it cannot return to the track in the direction <em>A</em> and also once it has left the station in the direction <em>B</em> it cannot return back to the station.</p>

### 입력 

 <p>The input consists of blocks of lines. Each block except the last describes one train and possibly more requirements for its reorganization. In the first line of the block there is the integer <em>N</em> described above. In each of the next lines of the block there is a permutation of 1, 2, ..., <em>N</em>. The last line of the block contains just 0.</p>

<p>The last block consists of just one line containing 0.</p>

### 출력 

 <p>The output contains the lines corresponding to the lines with permutations in the input. A line of the output contains Yes if it is possible to marshal the coaches in the order required on the corresponding line of the input. Otherwise it contains No. In addition, there is one empty line after the lines corresponding to one block of the input. There is no line in the output corresponding to the last “null” block of the input.</p>

