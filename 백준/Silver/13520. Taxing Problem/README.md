# [Silver I] Taxing Problem - 13520 

[문제 링크](https://www.acmicpc.net/problem/13520) 

### 성능 요약

메모리: 108384 KB, 시간: 84 ms

### 분류

이분 탐색, 구현

### 제출 일자

2025년 6월 18일 02:58:31

### 문제 설명

<p>George has won the lottery and, being a nice guy, has decided to spread the wealth around. However, monetary gifts can be taxed once they get over a certain size—the amount of tax depends on how much his friends have earned that year.</p>

<p>The amount of tax paid depends on tax bands. The bands start at zero. Each one takes a certain cut of income from the range of pre-tax income it covers. The final tax band applies to all income above its lower bound.</p>

<p>George is a savvy fellow and knows the number of tax bands, the amount of money each friend has earned and the amount he wants each friend to walk away with.</p>

<p>How much should George give to each friend before tax?</p>

### 입력 

 <ul>
	<li>One line containing an integer B (1 ≤ B ≤ 20): the number of tax bands.</li>
	<li>B further lines, each containing two real numbers: s<sub>i</sub> (0 < s<sub>i</sub> ≤ 10<sup>6</sup>): the size in pounds of the ith tax band, and p<sub>i</sub> (0 ≤ p<sub>i</sub> ≤ 100): the percentage taxation for that band.</li>
	<li>One line containing a real number P (0 ≤ P ≤ 99.999): the percentage tax on all income above other bands.</li>
	<li>One line containing an integer F, (0 < F ≤ 20): the number of friends George wants to pay.</li>
	<li>F further lines, each containing two real numbers e<sub>j</sub> and m<sub>j</sub> (0 ≤ e<sub>j</sub> ≤ 10<sup>6</sup>, 0 < m<sub>j</sub> ≤ 10<sup>6</sup>): the amount of money the jth friend has earned, and the amount of money they should receive after tax respectively.</li>
</ul>

<p>Tax bands will be given in increasing order.</p>

### 출력 

 <ul>
	<li>F lines, one for each friend specified in the input and in the same order.</li>
</ul>

<p>Each line should contain one real number: the amount of money George will give to his friend, in order to arrive at the correct amount after they have paid tax.<br>
All output must be accurate to an absolute or relative error of at most 10<sup>−6</sup>.</p>

