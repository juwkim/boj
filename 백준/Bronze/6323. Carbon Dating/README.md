# [Bronze I] Carbon Dating - 6323 

[문제 링크](https://www.acmicpc.net/problem/6323) 

### 성능 요약

메모리: 30888 KB, 시간: 64 ms

### 분류

수학(math)

### 문제 설명

<p>Until the second half of the 20th century, determining the actual age of an archaeological find had been more or less a matter of educated guessing. Comparing finds to previous, already dated, ones and evaluation of the surroundings of a find were the best available techniques.</p>

<p>But nowadays, there is a much more reliable method: carbon dating. Carbon dating works as follows: Naturally occurring carbon is a mixture of stable isotopes (mostly <sup>12</sup>C) and the unstable, radioactive, isotope <sup>14</sup>C. The ratio between the two is almost constant in living organisms: <sup>14</sup>C slowly decays, but at the same time, the radiation of the sun produces the same amount in the upper atmosphere, which is taken in by the organisms.</p>

<p>But when, for example, a tree is felled and made to wood, it does not receive any new <sup>14</sup>C, and the amount present in the wood becomes less and less due to radioactive decay. In this problem, you are to write a program that uses information about the amount of remaining <sup>14</sup>C to determine the approximate age of a sample. The following facts must be used:</p>

<ul>
	<li>The amount of <sup>14</sup>C present in a sample halves every 5730 years (this is called the half-life of <sup>14</sup>C).</li>
	<li>The rate of decay (measured in decays per hour per gram of carbon) is proportional to the amount of <sup>14</sup>C left in the sample.</li>
	<li>In living organisms (age zero), there are 810 decays per hour per gram of carbon.</li>
</ul>

<p>So, for example, if we measure in a sample of one gram of carbon 405 decays per hour, we know that it is approximately 5730 years old.</p>

<p style="text-align: center;"><img alt="" src="" style="height:364px; width:533px"></p>

### 입력 

 <p>The input file contains the measurements taken of several samples we want to date. Every line contains two positive integers, w and d. w is the amount of carbon in the sample, measured in grams, and d is the number of decays measured over one hour.</p>

<p>The input is terminated by a test case starting with w = d = 0.</p>

### 출력 

 <p>For each sample description in the input, first output the number of the sample, as shown in the sample output. The print the approximate age in the format</p>

<p style="text-align: center;"><strong>The approximate age is x years.</strong></p>

<p>If the age is less than 10,000 years, x should be rounded to the closest multiple of 100 years (rounding up in case of a tie). If the age is more then 10,000 years, round it to the closest multiple of 1000 years (again rounding up in case of a tie).</p>

<p>Print a blank line after each sample.</p>

