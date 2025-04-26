# [Silver I] Exotic Foods - 5132 

[문제 링크](https://www.acmicpc.net/problem/5132) 

### 성능 요약

메모리: 122288 KB, 시간: 112 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2025년 4월 26일 22:06:28

### 문제 설명

<p>Traveling through time is tiring and can really work up an appetite. Luckily, there is a huge variety of exotic foods to be found throughout time, such as dinosaur meat, dodo-bird eggs, mammoth milk, etc. Unfortunately, there is not enough space in the time machine to store a refrigerator, so if Tim wants to eat an exotic food, he must eat it right away. But, if he eats, he will become very full and will not be able to eat again while visiting the immediately following time period. Each food has a perceived value to Tim, and his goal is to maximize the total sum value for all the foods he actually eats. The order in which he visits the time periods has already been set and cannot be changed. By selectively choosing which foods he eats, what is the maximum total sum value he can achieve?</p>

### 입력 

 <p>The first line is the number K of input data sets, followed by the K data sets, each of the following form: The first line of each data set contains an integer n indicating the number of foods Tim will come across, where 1 ≤ n ≤ 50000. Next follows one line containing n integers vi, 1 ≤ vi ≤ 1000, indicating the values of the foods. The order of vi in the list is also the order in which Tim will encounter them.</p>

### 출력 

 <p>For each data set, output “Data Set x:” on a line by itself, where x is its number. On the next line, output the maximum sum of values Tim can achieve. Each data set should be followed by a blank line.</p>

