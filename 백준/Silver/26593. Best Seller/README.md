# [Silver V] Best Seller - 26593 

[문제 링크](https://www.acmicpc.net/problem/26593) 

### 성능 요약

메모리: 113112 KB, 시간: 116 ms

### 분류

구현(implementation), 정렬(sorting), 문자열(string)

### 문제 설명

<p>You run a store and want to know where you make the most money and which items sell the most. You have a list of your items, how many times each has sold and how much profit you make each sale. Each item name is a single word. The total profit on an item is the number of sales times the profit of the item. Write a program that will take in this data and produce a sorted list using the following rules:</p>

<p>Sorting Rules:</p>

<ul>
	<li>Sort items in descending order by total profit</li>
	<li>For items that have the same total profit, sort in descending order by number of sales</li>
	<li>For items that have the same total profit and number of sales, sort in ascending order by name</li>
</ul>

### 입력 

 <p>There will be an unknown number of inputs that consist of the triple itemName numberOfSales profitEachSale, with each triple on its own line, and each value on a line is separated by a single space. The itemName is a single word and the format for each input line will be:</p>

<pre>itemName numberOfSales profitEachSale</pre>

### 출력 

 <p>Display the sorted list, with each item on its own line. The format for displaying the item will be:</p>

<pre>$totalProfit – itemName/numberOfSales</pre>

<p>There is a single space before and after the dash, and the profit value must have exactly two decimal places.</p>

