# [Silver I] Exact Change - 4190 

[문제 링크](https://www.acmicpc.net/problem/4190) 

### 성능 요약

메모리: 111056 KB, 시간: 128 ms

### 분류

다이나믹 프로그래밍, 배낭 문제

### 제출 일자

2025년 5월 4일 00:44:00

### 문제 설명

<ul>
	<li>Seller: That will be fourteen dollars.</li>
	<li>Buyer: Here's a twenty.</li>
	<li>Seller: Sorry, I don't have any change.</li>
	<li>Buyer: OK, here's a ten and a five. Keep the change.</li>
</ul>

<p>When travelling to remote locations, it is often helpful to bring cash, in case you want to buy something from someone who does not accept credit or debit cards. It is also helpful to bring a variety of denominations in case the seller does not have change. Even so, you may not have the exact amount, and will have to pay a little bit more than full price. The same problem can arise even in urban locations, for example with vending machines that do not return change.</p>

<p>Of course, you would like to minimize the amount you pay (though you must pay at least as much as the value of the item). Moreover, while paying the minimum amount, you would like to minimize the number of coins or bills that you pay out.</p>

### 입력 

 <p>The first line of input contains one integer specifying the number of test cases to follow. Each test case begins with a line containing an integer, the price in cents of the item you would like to buy. The price will not exceed 10 000 cents (i.e., <span>$</span>100). The following line contains a single integer n, the number of bills and coins that you have. The number n is at most 100. The following n lines each contain one integer, the value in cents of each bill or coin that you have. Note that the denominations can be any number of cents; they are not limited to the values of coins and bills that we usually use in Canada. However, no bill or coin will have a value greater than 10 000 cents (<span>$</span>100). The total value of your bills and coins will always be equal to or greater than the price of the item.</p>

<p> </p>

### 출력 

 <p>For each test case, output a single line containing two integers: the total amount paid (in cents), and the total number of coins and bills used.</p>

