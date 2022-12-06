# [Silver V] Air Old Zeeland - 5092 

[문제 링크](https://www.acmicpc.net/problem/5092) 

### 성능 요약

메모리: 115160 KB, 시간: 148 ms

### 분류

자료 구조(data_structures), 구현(implementation), 트리를 사용한 집합과 맵(tree_set)

### 문제 설명

<p>Air Old Zeeland, or as it is informally known, Air OZ has taken to allowing customers to redeem their loyalty points for products. As it is only a recent idea, Air OZ is testing the market by offering a small but select number of products. Unfortunately the suppliers are not very good at keeping up with the demand and Air OZ decided to record the number of days a customer would have to wait for each product along with its listed price. This will enable them to get a feel for how many discontented customers they have</p>

### 입력 

 <p>Input will consist of a number of scenarios. The first line of each scenario contains a number N (0 < N <= 50) which represents the number of products in this offering. End of input is marked by a scenario with 0 products – this line should not be processed.</p>

<p>The product count is followed by N lines with each of Air OZ’s products listed on its own line. Each product name, which is limited to 20 characters and with no embedded spaces, is followed by the number of loyalty points needed to acquire the reward and the days to wait for it to be shipped to the purchaser. Each of these fields is separated by a single space. No product costs more than 1000 loyalty points and no product will be delayed by more than 100 days.</p>

<p>These N lines are followed by a line with the number of customers to be processed, C (0 < C <= 500). For each customer, there follows a line with the customer number, the number of products wishing to be purchased, P, and the maximum days they are prepared to wait for a product, M. (0 < P <= N, 0 < M <100) Each of these 3 numbers is separated by a single space. There follows P lines listing the products they wish to order, each on a single line.</p>

### 출력 

 <p>For each customer in a scenario, output the customer number followed by the value of their purchases, separated by a space, on a single line. If a product is not available within the timeframe set by the customer, then it is deemed that the product has not been bought, and that the customer is therefore discontented. On the same line, following the value, output an asterisk (*) if that customer has not purchased something they wanted due to shipping delays. The value and asterisk, if applicable, should be separated by a single space. The final line of each scenario's output contains the text "Number of discontented customers is: ", followed by the number of customers in that scenario who could not obtain all their products (ie the number of asterisks).</p>

