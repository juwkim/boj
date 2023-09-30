# [Silver V] We Want You Happy! - 30225 

[문제 링크](https://www.acmicpc.net/problem/30225) 

### 성능 요약

메모리: 115108 KB, 시간: 132 ms

### 분류

구현, 시뮬레이션

### 문제 설명

<p>The United Credit Finance (UCF) is running a simple scenario to see how many customers are happy with the company. UCF has one person (teller) serving the customers. Customers are numbered 1-n, and they arrive for service in sequential order, i.e., Customer 1 arrives first, then Customer 2, then Customer 3, etc. Also, no two customers arrive at the same time, i.e., Customer 2 will arrive later than Customer 1, Customer 3 will arrive later than Customer 2, etc. Customers are also processed in the order of arrival (i.e., not out of order).</p>

<p>As you might have noticed while waiting in a line, some customers get impatient and leave. Given the information about the UCF customers, you are to determine which customers are happy, i.e., they don’t leave before being processed.</p>

### 입력 

 <p>The first input line contains an integer, n (1 ≤ n ≤ 10<sup>3</sup>), indicating how many different customers are arriving. Each of the next n input lines contains the information about a customer as follows:</p>

<ul>
	<li>customer number (1, 2, 3, etc., in sequential order),</li>
	<li>arrival time (an integer between 1 and 10<sup>4</sup>, inclusive),</li>
	<li>service time (an integer between 1 and 10<sup>4</sup>, inclusive) indicating how long it will take the teller to process this customer (once the customer is at the teller),</li>
	<li>patience time (an integer between 1 and 10<sup>4</sup>, inclusive) indicating how long the customer will wait in line before giving up and leaving, i.e., if the customer is not at the teller, the customer will leave. Note that if a customer leaves, the teller will not process them, i.e., the customer will not take the teller’s time.</li>
</ul>

### 출력 

 <p>Print the happy customer numbers in sequential order (happy means they were processed, i.e., did not leave).</p>

