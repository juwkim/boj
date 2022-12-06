# [Bronze I] Toxic Assets - 5161 

[문제 링크](https://www.acmicpc.net/problem/5161) 

### 성능 요약

메모리: 30840 KB, 시간: 92 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>One of the reasons that home foreclosures have had such a huge impact on the economy is that various financial institutions invented mortgage-backed derivatives. Essentially, the right to the mortgage payments was packaged as an investment, i.e., sold to other investors in small chunks. These chunks might then be mixed with other investments, and repackaged and sold further. Thus, you have all kinds of derivatives whose real worth depends on mortgages hard to trace<sup>2</sup>. If you find out how the basic “building blocks” upon which all the derivatives rely are changing in value, it might not be at all obvious to find out what your portfolio is really worth now. You might have to track it through a chain of derivatives.</p>

<p>Here is how we will model this. You have some basic investments, such as mortgages. For each of those, we assume that one unit was worth \$1 before, and we will tell you how much it is worth now. Then, we have derivatives. Each derivative will be composed of one or more basic investments or other derivatives. You will get a list of other investments, together with the percentage that they contribute to the derivative (those percentages will add up, of course). We will ensure that each derivative will only contain basic investments, or derivatives with a lower number. In particular, there will be no cycles. Finally, we will give you the percentages of investments in your portfolio. Your goal is to calculate how much one unit of your portfolio (which was initially worth \$1) is worth now.</p>

<p><sup>2</sup>This description is certainly an oversimplification. It’s as best as we understand what is happening. In fact, another reason that the economy is not doing so well is that very few people actually understood how these derivatives work.</p>

### 입력 

 <p>The first line contains the number K of data sets. This is followed by K data sets, each of the following form:</p>

<p>The first line of each data set contains two integer numbers B,D, the number of basic investments (1 ≤ B ≤ 100) and the number of derivatives (0 ≤ D ≤ 100). We will number the basic ones 1,... ,B, and the derivatives B + 1,... ,B + D. This is followed by a line with B non-negative floating point numbers, the current values of one unit of each of the basic investments in order.</p>

<p>Next will be D lines. The dth line will consist of B + d − 1 non-negative floating point numbers, describing the percentage of investment B +d that is made up of investments 1,... ,B +d−1. These numbers will always add up to 1. No derivative ever contains parts of a derivative with a higher number.</p>

<p>Finally, there will be one more line with B + D non-negative floating point numbers (adding up to 1). This line tells you what percentage of your portfolio is made up of each of the investments.</p>

### 출력 

 <p>For each data set, output “Data Set x:” on a line by itself, where x is its number. On the next line, output the current value of one unit of your portfolio, rounded to two decimals. Each data set should be followed by one empty line.</p>

