# [Silver V] Jumping Frog - 26316 

[문제 링크](https://www.acmicpc.net/problem/26316) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

그리디 알고리즘(greedy)

### 문제 설명

<p>Freddy the frog is trying to go get a bite to eat. The problem is Freddy lives far away from all the restaurants he likes. Freddy is a capable frog, able to jump over a large number of cells. Unfortunately, on a given day, Freddy may be too hungry to jump very far. On a given day, he can only jump over at most d cells (note that he can also jump over fewer cells).</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/0b41642a-d0ea-425c-8fbc-1cc3c888a993/-/preview/" style="width: 321px; height: 123px;"></p>

<p>Another complication for Freddy is the path he jumps across is always under construction. Some of the cells are blocked off! Freddy doesn’t want to land in a cell under construction but is allowed to jump over them.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/e5196092-ae70-4b43-bc97-191d8a928ce7/-/preview/" style="width: 632px; height: 132px;"></p>

<p>Freddy starts off in the first cell and must travel to the last cell where his destination restaurant resides. He would like to know if he can reach the last cell and how quickly he can reach it. Freddy always jumps towards his destination.</p>

<p>Given a description of cells, determine the minimum number of jumps Freddy can make to reach the restaurant.</p>

### 입력 

 <p>The first input line contains a positive integer, n, indicating the number of days to check. Each day is represented by two lines. The first line of each day contains two integers, c (2 ≤ c ≤ 50) and d (0 ≤ d ≤ 50), representing (respectively) the number of cells in the path from Freddy’s home to the restaurant (including his home and the restaurant) and the maximum number of cells Freddy can jump over in a single jump on that day. The second line is a string consisting of c characters containing only ‘.’ and ‘X’ characters where ‘.’ represents that the cell is okay for Freddy to occupy and ‘X’ represents that the cell is blocked by construction. The first and last characters of the string represent Freddy’s home and the restaurant, respectively; these two locations will never be blocked.</p>

### 출력 

 <p>For each day, first output the heading “Day #d”, where d is the day number, starting with 1. Then, print the input values exactly as they appear in the input. Following the header info, output the minimum number of jumps it takes Freddy to reach the restaurant. If it is not possible to reach the restaurant on a given day, print the number 0 instead.</p>

<p>Leave a blank line after the output for each data set. Follow the format illustrated in Sample Output.</p>

