# [Bronze II] Olympic Ranking - 23334 

[문제 링크](https://www.acmicpc.net/problem/23334) 

### 성능 요약

메모리: 47516 KB, 시간: 112 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>The Olympic Games are the most important sporting events in human history. Usually, the Olympic Games are held every four years. However, the 2020 Olympic Games just finished in August 2021 due to the COVID-19 outbreaks.</p>

<p>There are more than 200 nations participating in the Olympic Games. Thousands of athletes around the world compete in various sports. The athletes represent their countries or National Olympic Committees (NOCs) to compete for medals. Therefore, each country or NOC may win medals in the competitions.</p>

<p>There are three types of medals: gold medals, silver medals, and bronze medals. Typically, the gold medals are awarded to the winners of the competitions, and silver medals are awarded to the runner-ups. Most of the bronze medals are awarded to the second runner-ups. However, there can be no second runner-up in some sports. The bronze medals can be awarded in different manners. For example, in a few tournament sports, such as wrestling, boxing, and judo, two bronze medals are awarded to the eliminated semi-finalists.</p>

<p>A country or NOC has a better rank than another country or NOC if one of the following conditions holds.</p>

<ol>
	<li>It wins more gold medals.</li>
	<li>It wins the same amount of gold medals, and it wins more silver medals.</li>
	<li>It wins the same amount of gold medals and silver medals, and it wins more bronze medals.</li>
</ol>

<p>Please write a program to find the country or NOC which has the best rank among all countries and NOCs.</p>

### 입력 

 <p>The first line of the input contains one positive integer n. Then n lines follow. Each of the following lines contains three non-negative integers g, s, b, and the name of a country or NOC. They are separated by blanks.</p>

### 출력 

 <p>Print the name of the country or NOC of the best rank.</p>

