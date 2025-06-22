# [Silver I] Logarithmic Paprika - 8346 

[문제 링크](https://www.acmicpc.net/problem/8346) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

수학

### 제출 일자

2025년 6월 23일 01:14:29

### 문제 설명

<p>The best selling vegetable in Byteland is logarithmic paprika. As the name of this great vegetable suggests, the weight of each paprika is the power of 2 grams. The lightest paprika weighs 2<sup>0</sup> grams, while the largest one weighs 2<em><sup>k</sup></em> grams.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/4a47d5b8-3f08-476f-bb85-bd8ca44d89cf/-/preview/" style="width: 320px; height: 240px;"></p>

<p>Residents of Byteland don't like buying pieces of paprika and so salesmen are forced to sell only whole paprika. What is more, bytean people are very exact and they do not tolerate situations when salesman is not able to sell the exact weight of paprika they are willing to buy. This causes stress among all salesmen of Byteland - some cases of insomnia have been observed as well. One of your friends, who owns vegetable garden, asked you to write a program which is supposed to help salesmen.</p>

<p>Write a program which:</p>

<ul>
	<li>reads a description of the current stock of paprika from the standard input,</li>
	<li>determines the smallest weight of a paprika that cannot be weighed without cutting any paprika,</li>
	<li>writes the result to the standard output.</li>
</ul>

### 입력 

 <p>The first line of the input contains one integer <em>k</em> (1 ≤ <em>k</em> ≤ 10), meaning that weights of available paprika are from the set 2<sup>0</sup>, 2<sup>1</sup>, ..., 2<em><sup>k</sup></em>. Second line contains <em>k</em> + 1 positive integers <em>p</em><sub>0</sub>, <em>p</em><sub>1</sub>, ..., <em>p<sub>k</sub></em> not greater than 1 000, separated with single spaces and representing the current stock: <em>p</em><sub>0</sub> paprika of weight 1 gram, <em>p</em><sub>1</sub> - of weight 2 grams, ..., <em>p<sub>k</sub></em> - of weight 2<em><sup>k</sup></em> grams.</p>

### 출력 

 <p>The first and only line of the output should contain one positive integer <em>x</em> - the smallest weight that cannot be weighed without cutting any paprika.</p>

