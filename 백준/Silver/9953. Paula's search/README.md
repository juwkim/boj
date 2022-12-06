# [Silver V] Paula's search - 9953 

[문제 링크](https://www.acmicpc.net/problem/9953) 

### 성능 요약

메모리: 113112 KB, 시간: 112 ms

### 분류

이분 탐색(binary_search), 구현(implementation)

### 문제 설명

<p>Paula is searching for the perfect pink ball dress. In her High Street are 100 shops spread evenly along both sides of the street, odd numbers on one side, even numbers on the other as usual.</p>

<p>Paula always begins her search by going into the nearest shop to her home, which is shop 50, right in the middle of the even numbered side of the road. The shop owners all know where her dress of choice is, but they like to offer Paula a challenge, so they have agreed to tell her only one of 4 things:</p>

<ol>
	<li>Yes, I have the perfect dress for you!</li>
	<li>You are on the wrong side of the road, cross over.</li>
	<li>You need to look down this side of the street (amongst the lower numbered shops).</li>
	<li>You need to look up this side of the street (amongst the higher numbered shops).</li>
</ol>

<p>If Paula gets answer 1, she buys the dress and goes home. If she gets answers 2, 3 or 4, Paula always goes to the mid point of the block of shops in which she has to search (if there is an even number of shops, she goes to the lower numbered of the two middle shops). Here the shop owner gives her one of the 4 responses and Paula continues her search if necessary.</p>

### 입력 

 <p>Input will be a number of scenarios, each one being a single integer (between 1 and 100 inclusive) on a line on its own representing the number of the shop where Paula will find her perfect pink ball dress. Input will be terminated by a single 0, this line should not be processed.</p>

### 출력 

 <p>Output will be a single integer (on a line on its own) for each line of input. The integer will be the number of shops Paula had to visit in order to buy her dress.</p>

