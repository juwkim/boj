# [Bronze I] Currency Exchange - 7361 

[문제 링크](https://www.acmicpc.net/problem/7361) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

사칙연산(arithmetic), 수학(math)

### 문제 설명

<p>When Issac Bernand Miller takes a trip to another country, say to France, he exchanges his US dollars for French francs. The exchange rate is a real number such that when multiplied by the number of dollars gives the number of francs. For example, if the exchange rate for US dollars to French francs is 4.81724, then 10 dollars is exchanged for 48.1724 francs. Of course, you can only get hundredth of a franc, so the actual amount you get is rounded to the nearest hundredth. (We'll round .005 up to .01.) All exchanges of money between any two countries are rounded to the nearest hundredth.</p>

<p>Sometimes Issac's trips take him to many countries and he exchanges money from one foreign country for that of another. When he finally arrives back home, he exchanges his money back for US dollars. This has got Issac thinking about how much if his unspent US dollars is lost (or gained!) to these exchange rartes. You'll compute how much money Issac ends up with if he exchanges it many times. You'll always start with US dollars and you'll always end with US dollars.</p>

### 입력 

 <p>The first 5 lines of input will be the exchange rates between 5 countries, numbered 1 through 5. Line i will five the exchange rate from country i to each of the 5 countries. Thus the jth entry of line i will give the exchange rate from the currency of country i to the currency of country j. the exchange rate form country i to itself will always be 1 and country 1 will be the US. Each of the next lines will indicate a trip and be of the form</p>

<p>N c<sub>1</sub> c<sub>2</sub> … c<sub>n</sub> m</p>

<p>Where 1 <= n <= 10 and c<sub>1</sub>, …, c<sub>n</sub> are integers from 2 through 5 indicating the order in which Issac visits the countries. (A value of n = 0 indicates end of input, in which case there will be no more numbers on the line.) So, his trip will be 1 -> c<sub>1</sub> -> c<sub>2</sub> -> … -> c<sub>n</sub> -> 1. the real number m will be the amount of US dollars at the start of the trip.</p>

### 출력 

 <p>Each trip will generate one line of output giving the amount of US dollars upon his return home from the trip. The amount should be fiven to the nearest cent, and should be displayed in the usual form with cents given to the right of the decimal point, as shown in the sample output. If the amount is less than one dollar, the output should have a zero in the dollars place.</p>

<p> </p>

