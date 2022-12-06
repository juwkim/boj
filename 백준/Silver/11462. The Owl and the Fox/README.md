# [Silver V] The Owl and the Fox - 11462 

[문제 링크](https://www.acmicpc.net/problem/11462) 

### 성능 요약

메모리: 116984 KB, 시간: 224 ms

### 분류

이분 탐색(binary_search), 브루트포스 알고리즘(bruteforcing), 런타임 전의 전처리(precomputation)

### 문제 설명

<p>Fox Mithra has finally learned the numbers and he is now familiar with the concept of ‘one’, ’two’, ‘three’ and also even ‘zero’, ‘minus one’, ‘minus two’ and so on. Really, an achievement for such a small fox. He took the textbook and copied the integers from the book one by one from the smallest to the biggest on the wall of his enclosure in the ZOO.</p>

<p>“Look, there is something wrong with your sequence on the wall”, said the owl who just landed on the branch above Mithra’s head. “You should put 30 between 20 and 22, there.”</p>

<p>“Why?”</p>

<p>“Because the importance of a number is judged by the sum of its digits. 30 is therefore less important than 22 and it is more important than 20. And obviously, 30 should be equally close to 20 and 22 because its sum of digits differs only by one from both 20 and 22.”</p>

<p>“I see,” replied Mithra, “you are really clever. Can you help me please to rearrange the sequence correctly? Each time I tell you a number N you will tell me the closest smaller number with sum of digits less by one than the sum of digits of N.”</p>

<p>“With pleasure,” nodded the owl majestically.</p>

<p>Your task is to imitate the owl’s task. Given an integer N you have to find the biggest integer which is smaller than N with sum of digits less by one than the sum of digits of N.</p>

### 입력 

 <p>There are more test cases. Each case consists of a line containing a single integer N (1 ≤ N ≤ 100 000). The input is terminated by a line containing string “END” and no other symbols.</p>

### 출력 

 <p>For each test case print on a separate line the number demanded by fox Mithra.</p>

