# [Silver V] Grocery Shopping - 5134 

[문제 링크](https://www.acmicpc.net/problem/5134) 

### 성능 요약

메모리: 113112 KB, 시간: 132 ms

### 분류

자료 구조(data_structures), 구현(implementation), 문자열(string)

### 문제 설명

<p>Vint Cerf and Bob Kahn, curious about the users of their network, decide to invite them all to a barbecue. The amount of traffic on the network suggests that they will need a lot of food. Given the grocery store’s inventory and their grocery list, figure out how much money they will save by using their grocery store’s club card, which allows them to purchase some items at a cheaper price.</p>

### 입력 

 <p>The first line is the number K of input data sets, followed by the K data sets, each of the following form:</p>

<p>The first line of each data set contains two integers 1 ≤ N, M ≤ 100, where N is the number of different items in the grocery store and M is the number of different items in the grocery list.</p>

<p>This is followed by N lines, each describing an item in the grocery store. Each line i has an integer n<sub>i</sub>, the quantity of this item currently in stock, followed by two dollar amounts \$0.00 ≤ p<sub>i</sub>, c<sub>i</sub> ≤ \$99.99, which are the normal price and the club card price respectively. This is followed by a space and then a string s<sub>i</sub>, the name of the item, which can contain upper and lower case letters and spaces.</p>

<p>This is followed by M lines, each describing an item on the grocery list. Each line j has an integer m<sub>j</sub>, the quantity desired of this item, followed by a space and then a string s<sub>j</sub>, the name of the item, which can contain upper and lower case letters and spaces.</p>

<p>An item on the grocery list is the same as an item in the grocery store’s inventory if its name is the same, ignoring case. There will be no extra leading or trailing white space in the names given in the input.</p>

### 출력 

 <p>For each data set, output “Data Set x:” on a line by itself, where x is its number. On the next line, output the exact dollar amount saved by using the club card, no commas necessary. Each data set should be followed by a blank line.</p>

