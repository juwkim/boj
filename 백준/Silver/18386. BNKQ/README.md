# [Silver II] BNKQ - 18386 

[문제 링크](https://www.acmicpc.net/problem/18386) 

### 성능 요약

메모리: 112308 KB, 시간: 108 ms

### 분류

구현, 정렬

### 제출 일자

2025년 3월 29일 10:40:14

### 문제 설명

<p>Nili bank provides banking services to its customers throughout the country. In each of their branches they have multiple tellers (cashier) that provide deposit or withdraw services to customers. Each teller has a queue of customers that are waiting for depositing or withdrawing money from their account through the teller. The bank records customer, the time they stand in queue (or processed), and teller information.</p>

<p>With the information in their hand, bank want to know which tellers were the busiest and what is their peak time frame during the day.</p>

<p>Write a program that receive the records for a single day as input and print the top three busiest tellers and their peak time frame.</p>

### 입력 

 <p>First N lines (N < 10000) contains the records for a single day.</p>

<ul>
	<li>Record format: TELLERCUSTOMER[TIME]</li>
	<li>TELLER, is the teller id</li>
	<li>CUSTOMER, is the customer id</li>
	<li>TIME, is the time (between 08:00:00AM - 04:00:00PM) customer stands in queue, or was processed by the teller</li>
	<li>First occurrence of record is for customer standing in queue, Second occurrence of the same record is for the time customer being processed</li>
	<li>[TIME], it is absent in the record if customer leave the queue without processing. Input ends with the line ENDOFINPUT. It is not part of input.</li>
</ul>

### 출력 

 <p>Print top 3 busiest tellers, total number of customer they have processed in a day and his/her peak time frames (in hours); each teller in one line.</p>

<ul>
	<li>Format: TELLERPROCESSED-COUNTPEAK-TIMEFRAME</li>
	<li>Being a busy teller means processing more customers, not having more customers in queue.</li>
	<li>Print the first PEAK-TIMEFRAME (the one nearest to 08:00:00AM) for each teller, if there are multiple time frames with same peak weight.</li>
	<li>Sort tellers by name in ascending order if two or more teller have processed same number of customers.
	<ul>
		<li>TIMEFRAME, each time frame is 1 hour in length. Eg: These are 8 timeframes between 08:00AM - 04:00PM: 08AM, 09AM, 10AM, ... 02PM, and 03PM</li>
		<li>A time frame is, eg:
		<ul>
			<li>08:00:00AM <= 08AM time frame < 09:00:00AM</li>
			<li>03:00:00PM <= 03PM time frame < 04:00:00PM</li>
		</ul>
		</li>
	</ul>
	</li>
</ul>

