# [Silver I] Pearls - 7903 

[문제 링크](https://www.acmicpc.net/problem/7903) 

### 성능 요약

메모리: 109544 KB, 시간: 96 ms

### 분류

다이나믹 프로그래밍, 누적 합

### 제출 일자

2025년 5월 6일 07:56:54

### 문제 설명

<p>In Pearlania everybody is fond of pearls. One company, called The Royal Pearl, produces a lot of jewelry with pearls in it. The Royal Pearl has its name because it delivers to the royal family of Pearlania. But it also produces bracelets and necklaces for ordinary people. Of course the quality of the pearls for these people is much lower then the quality of pearls for the royal family. In Pearlania pearls are separated into 100 different quality classes. A quality class is identified by the price for one single pearl in that quality class. This price is unique for that quality class and the price is always higher then the price for a pearl in a lower quality class.</p>

<p>Every month the stock manager of The Royal Pearl prepares a list with the number of pearls needed in each quality class. The pearls are bought on the local pearl market. Each quality class has its own price per pearl, but for every complete deal in a certain quality class one has to pay an extra amount of money equal to ten pearls in that class. This is to prevent tourists from buying just one pearl.</p>

<p>Also The Royal Pearl is suffering from the slow-down of the global economy. Therefore the company needs to be more efficient. The CFO (chief financial officer) has discovered that he can sometimes save money by buying pearls in a higher quality class than is actually needed. No customer will blame The Royal Pearl for putting better pearls in the bracelets, as long as the prices remain the same.</p>

<p>For example 5 pearls are needed in the 10 Euro category and 100 pearls are needed in the 20 Euro category. That will normally cost: (5 + 10) × 10 + (100 + 10) × 20 = 2350 Euro. Buying all 105 pearls in the 20 Euro category only costs: (5 + 100 + 10) × 20 = 2300 Euro.</p>

<p>The problem is that it requires a lot of computing work before the CFO knows how many pearls can best be bought in a higher quality class. You are asked to help The Royal Pearl with a computer program.</p>

<p>Given a list with the number of pearls and the price per pearl in different quality classes, give the lowest possible price needed to buy everything on the list. Pearls can be bought in the requested, or in a higher quality class, but not in a lower one.</p>

### 입력 

 <p>The first line of the input contains the number of test cases. Each test case starts with a line containing the number of categories c (1 ≤ c ≤ 100). Then, c lines follow, each with two numbers a<sub>i</sub> and p<sub>i</sub>. The first of these numbers is the number of pearls a<sub>i</sub> needed in a class (1 ≤ a<sub>i</sub> ≤ 1000). The second number is the price per pearl p<sub>i</sub> in that class (1 ≤ p<sub>i</sub> ≤ 1000). The qualities of the classes (and so the prices) are given in ascending order. All numbers in the input are integers.</p>

### 출력 

 <p>For each test case a single line containing a single number: the lowest possible price needed to buy everything on the list.</p>

