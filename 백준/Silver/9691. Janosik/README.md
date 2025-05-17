# [Silver I] Janosik - 9691 

[문제 링크](https://www.acmicpc.net/problem/9691) 

### 성능 요약

메모리: 108384 KB, 시간: 96 ms

### 분류

수학, 정수론

### 제출 일자

2025년 5월 18일 08:26:09

### 문제 설명

<p>Janosik, otherwise known as Robin Hood, takes the rich to distribute to the poor. Together with his gang they robbed a convoy carrying gold to the counts' castle and <em>n</em> caskets fell prey to robbers. After transporting their loot to the cave it turned out that <em>i</em>-th (for <em>i</em> = 1, 2, ..., <em>n</em>) casket contains exactly <em>i</em> money-bags full of gold.</p>

<p>In case a poor man comes to Janosik asking for a few gold ducats, Janosik utilises the following procedure. Firstly he chooses a non-empty casket that contains the smallest number of money-bags containing gold. In case the casket contains exactly only one money-bag, Janosik hands it to the man in need, and sees him go away happily. Otherwise, if the casket contains an odd number of money-bags, Janosik puts one of the money-bags in his pocket, and starts the whole process again. However, in case there is an even number of money-bags, Janosik takes exactly half of them out and puts them in an empty casket (luckily the empty caskets are plentiful in the cave) and begins the whole procedure anew. Therefore if a penniless man comes to Janosik, and in case he still will be in a possession of at least one non-empty casket, as a result of (possibly multiple) employment of Janosik's procedure, the poor man is sure to get the money-bag full of gold. The poor would come to the Janosik's cave until all the caskets are empty.</p>

<p>Fellow robbers from Janosik's gang wonder if their leader does not ruin the good name of thugs with his behaviour. They want to know how many looted money-bags remain in Janosik's pocket when all the caskets are empty.</p>

### 입력 

 <p>The first and only line of the input contains one integer <em>n</em> (1 ≤ <em>n</em> ≤ 10<sup>9</sup>), which indicates the number of caskets robbed by Janosik's gang.</p>

### 출력 

 <p>The first and only line of output should contain an integer representing the number of money-bags with gold, which will remain in Janosik's pocket after emptying all the caskets.</p>

