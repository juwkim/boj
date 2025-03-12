# [Silver II] Painting Floors - 11074 

[문제 링크](https://www.acmicpc.net/problem/11074) 

### 성능 요약

메모리: 120180 KB, 시간: 148 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 3월 13일 04:38:21

### 문제 설명

<p>I really need to paint my floor! My floor is rectangular and has some furniture on it. Instead of hiring someone to paint it for me, I decided to do it myself. So I went out the local paint store, Antonio’s Colourful Masterpieces, and asked for some paint. The man behind the counter asked me if I would like to try some experimental paint. Curious as to what could be experimental about paint, I said, “Yes!” I then purchased 1 000 paint cans and went home (it was on a very good sale).</p>

<p>When I got home, I opened the instruction manual for the paint and was extremely surprised:</p>

<blockquote>
<p>“When you pour the whole can of paint onto the ground, it will fill in the 1 × 1 block of floor it is in and then will expand out and fill every square that is in the same row or same column as the original 1 × 1 block so long as there is not an obstacle in the way.”</p>
</blockquote>

<p>For example, in the left room, the paint is poured in the third row and second column and it fills in coloured squares. In the right room, the paint is poured in the same square, but it only goes until it hits the black obstacle (piece of furniture).</p>

<p style="text-align:center"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/11074/1.png" style="height:202px; width:466px"></p>

<p>You may not pour paint onto any of the furniture (obviously!). The goal is to paint every square in the room that is not furniture. Painted squares do not become obstacles for future pours of paint and it is okay to paint squares multiple times.</p>

<p>For small rooms, I can easily figure out how to paint the rooms with this experimental paint, but for large rooms, I’m worried that I will run out of paint before I finish the floor! Can you tell me where to pour the paint? You do not need to give me an optimal solution, but you must give me a solution that uses no more than the 1 000 paint cans that I purchased. It is guaranteed that 1 000 paint cans are enough to paint the floor.</p>

### 입력 

 <p>The input contains one test case.</p>

<p>The first line will contain two integers m and n (1 ≤ m, n ≤ 500) being the dimensions of my room in metres. The next m lines will contain n characters each. These lines will show the layout of my room. The map of the rooms will only contain the characters ‘.’ and ‘x’. An ‘x’ denotes an obstacle in the room and a ‘.’ denotes no obstacle. There will be at most 500 x’s in the input.</p>

### 출력 

 <p>The output will consist of several lines. In each line, output two integers: the row and the column of where to pour the ith can of paint. The rows and columns are 1-based from the top-left corner. The number of lines of output must be no more than 1 000. The lines need not be in any particular order. Any valid output will be considered correct.</p>

