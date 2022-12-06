# [Bronze II] DVDs - 5103 

[문제 링크](https://www.acmicpc.net/problem/5103) 

### 성능 요약

메모리: 45544 KB, 시간: 156 ms

### 분류

구현(implementation), 시뮬레이션(simulation), 문자열(string)

### 문제 설명

<p>A local company, “DVDs R Us”, need your help with a stock management system. They sell DVDs on-line from a local warehouse and need to know at any moment how many DVDs of each title they have in stock.</p>

<p>DVDs of a particular title have a stock code and are allocated a certain amount of storeage space in the warehouse. The more popular a DVD title is, the more space is allocated. DVDs are continually being sold and replaced, hence the need for a system to keep track of how many are in stock.</p>

### 입력 

 <p>Input consists of data about a number of DVD titles. The data for a DVD title begins with a stock code, a 7 character code consisting of upper case letters and digits only. Input is terminated by a code consisting of a single # - do not process this title.</p>

<p>The next line for each title consists of two integers, M and S, separated by a space. M is the maximum number of DVDs of that title that can be held in stock at any one time (20 <= M <= 500). S is the number of that title currently in stock (0 <= S <= M).</p>

<p>The third line is a single integer, T, the number of transactions to follow (0 < T <= 100). There then follow T lines, each containing details of 1 transaction. A transaction line consists of a single upper case letter (S or R), followed by a space, followed by a positive integer less than 1000.</p>

<ul>
	<li>If the letter is S it represents a sale, in which case the number shows how many of the DVD have been sold. If the sale is for more than the current stock, only those DVDs currently in stock may be sold.</li>
	<li>If the letter is R it is a restock, so the number shows how many DVDs are added to the current stock. If this would take the number of DVDs in stock to more than the maximum, then the extra items have to be sent back. </li>
</ul>

### 출력 

 <p>Output consists of the DVD's stock code, followed by a space, followed by the number in stock at the end of all the transactions.</p>

