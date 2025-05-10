# [Silver I] Argus - 6235 

[문제 링크](https://www.acmicpc.net/problem/6235) 

### 성능 요약

메모리: 111440 KB, 시간: 152 ms

### 분류

자료 구조, 구현, 우선순위 큐

### 제출 일자

2025년 5월 11일 06:47:53

### 문제 설명

<p>A data stream is a real-time, continuous, ordered sequence of items. Some examples include sensor data, Internet traffic, financial tickers, on-line auctions, and transaction logs such as Web usage logs and telephone call records. Likewise, queries over streams run continuously over a period of time and incrementally return new results as new data arrives. For example, a temperature detection system of a factory warehouse may run queries like the following. </p>

<ul>
	<li>Query-1: "Every five minutes, retrieve the maximum temperature over the past five minutes." </li>
	<li>Query-2: "Return the average temperature measured on each floor over the past 10 minutes."</li>
</ul>

<p>We have developed a Data Stream Management System called Argus, which processes the queries over the data streams. Users can register queries to the Argus. Argus will keep the queries running over the changing data and return the results to the corresponding user with the desired frequency. </p>

<p>For the Argus, we use the following instruction to register a query: </p>

<ul>
	<li>Register Q_num Period</li>
</ul>

<p>Q_num (0 < Q_num <= 3000) is query ID-number, and Period (0 < Period <= 3000) is the interval between two consecutive returns of the result. After Period seconds of register, the result will be returned for the first time, and after that, the result will be returned every Period seconds. </p>

<p>Here we have several different queries registered in Argus at once. It is confirmed that all the queries have different Q_num. Your task is to tell the first K queries to return the results. If two or more queries are to return the results at the same time, they will return the results one by one in the ascending order of Q_num. </p>

### 입력 

 <p>The first part of the input are the register instructions to Argus, one instruction per line. You can assume the number of the instructions will not exceed 1000, and all these instructions are executed at the same time. This part is ended with a line of "#". </p>

<p>The second part is your task. This part contains only one line, which is one positive integer K (<= 10000). </p>

### 출력 

 <p>You should output the Q_num of the first K queries to return the results, one number per line.</p>

<p> </p>

