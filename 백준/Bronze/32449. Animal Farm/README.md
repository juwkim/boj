# [Bronze III] Animal Farm - 32449 

[문제 링크](https://www.acmicpc.net/problem/32449) 

### 성능 요약

메모리: 113716 KB, 시간: 124 ms

### 분류

구현

### 제출 일자

2024년 10월 6일 11:35:36

### 문제 설명

<p>On Animal Farm, the animals have rebelled against their human owner and have taken over the management of the farm. To ensure equality and fairness among all the animals, they have decided to create a new set of rules. However, as the new leaders, the pigs have started making changes to the rules to favor themselves.</p>

<p>The farm maintains a hierarchy of animals based on their species, with each animal assigned a specifc infuence level. This infuence level, represented as a positive integer, determines the animal’s priority in decision-making. Within a group, an animal can make decisions if it has the highest influence level among the members.</p>

<p>The pigs have a plan to maximize their collective infuence in the leadership council by selecting a specific group of animals. Given a list of animals with their species and influence levels, you are tasked to form the most influential leadership council while adhering to the following rules:</p>

<ol>
	<li>Only one pig species is allowed in the council to avoid power conflicts among the pigs.</li>
	<li>Every council member of non-pig species should have an influence level less than the influence level of the only pig’s in the council.</li>
</ol>

<p>Determine the maximum total influence levels of the council that can be formed under these rules.</p>

### 입력 

 <p>The first line contains an integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container>, representing the number of animals. The next <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> lines each contain a string <code>species</code> and a positive integer <code>influence</code>:</p>

<ul>
	<li><code>species</code> is a string representing the species of the animal, e.g., “<code>pig</code>”, “<code>horse</code>”, “<code>cow</code>”, etc.</li>
	<li><code>influence</code> is an integer representing the influence level of the animal.</li>
</ul>

### 출력 

 <p>Output a single integer, the maximum total influence levels of the leadership council that can be formed following the rules.</p>

