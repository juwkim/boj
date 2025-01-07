# [Silver II] Beth’s Cookies - 30572 

[문제 링크](https://www.acmicpc.net/problem/30572) 

### 성능 요약

메모리: 108384 KB, 시간: 92 ms

### 분류

자료 구조, 구현, 스택

### 제출 일자

2025년 1월 8일 06:58:03

### 문제 설명

<p>This is the story Alph told his schoolmate Beth. “Last vacations, I went exploring that big abandoned house in the woods above the dam lake. I was very proud at that time to be freshly admitted to Tomorrow Programming School, and so I decided to stick to firm and clear rules of exploration and to make a log of my actions.</p>

<p>Inside the house, there were only rooms connected by doors between them. No corridors, no hallways. Whenever I entered a room for the second, third, etc. time, I did it always through the door by which I had left it last time. Whenever I went through a door I wrote down one letter. When I moved from a room to an adjacent room which was either undiscovered yet or which I had discovered later than the current room, I wrote down F, like Forward. When I moved to a room which I had discovered earlier than the current room, I wrote down B, like Backward. By discovery of a room I mean entering the room for the first time.</p>

<p>I started and finished my exploration in the entrance room of the house. When I finally left the house, I had a sequence of letters, in the order I wrote them down during my exploration. Later, to make it more suitable for some future automated processing, I substituted each <code>F</code> by an opening bracket and each <code>B</code> by a closing bracket. Here is my modified sequence. Do you think it can be used for some unusual programming task?”</p>

<p>It took Beth only seconds to reply. “Surely, it can be used. Insert symbol <code>*</code> between each )( pair. Insert symbol <code>1</code> between each <code>()</code> pair. And also, insert pair of symbols <code>+1</code> between each <code>))</code> pair. It will result in an arithmetic expression, and I will give you as many cookies, as will be the value of the expression, but you have to calculate it first, obviously.”</p>

### 입력 

 <p>The first input line contains even integer N (2 ≤ N ≤ 100), the length of the sequence of bracket which resulted from Alph’s exploration. The second line contains the sequence itself, without any spaces or additional symbols.</p>

### 출력 

 <p>Output the number of cookies Alph will receive from Beth.</p>

