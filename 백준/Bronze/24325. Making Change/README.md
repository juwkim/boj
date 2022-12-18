# [Bronze I] Making Change - 24325 

[문제 링크](https://www.acmicpc.net/problem/24325) 

### 성능 요약

메모리: 113112 KB, 시간: 112 ms

### 분류

구현(implementation)

### 문제 설명

<p>Anakin Skywalker is leaving Tatoonie, but before he can go he must program a droid to do his old job of making change for customers at Watto’s junk business. Given the price of an item and the payment determine the correct change using <span>$</span>50, <span>$</span>20, <span>$</span>10, <span>$</span>5, and <span>$</span>1 bills. You don’t have to worry about change, because Watto always keeps the change.</p>

### 입력 

 <p>A positive integer, n, on the first line indicating the number of data sets to follow. Each data set will consist of two positive numbers. The first is the cost to the customer and the second is the payment made by the customer. The payment will always be greater than the cost.</p>

### 출력 

 <p>For each data set print the correct change on one line using the format</p>

<pre>v-$50, w-$20, x-$10, y-$5, z-$1</pre>

<p>where v, w, x, y, z are the number of bills needed to make the correct change. Of course, the correct change will always use larger bills when possible (i.e., 1-<span>$</span>5 not 5-<span>$</span>1)</p>

