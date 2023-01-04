# [Silver IV] Fractiles (Small) - 14387 

[문제 링크](https://www.acmicpc.net/problem/14387) 

### 성능 요약

메모리: 114488 KB, 시간: 128 ms

### 분류

수학(math), 정수론(number_theory)

### 문제 설명

<p>Long ago, the Fractal civilization created artwork consisting of linear rows of tiles. They had two types of tile that they could use: gold (<code>G</code>) and lead (<code>L</code>).</p>

<p>Each piece of Fractal artwork is based on two parameters: an original sequence of K tiles, and a complexity C. For a given original sequence, the artwork with complexity 1 is just that original sequence, and the artwork with complexity X+1 consists of the artwork with complexity X, transformed as follows:</p>

<ul>
	<li>replace each <code>L</code> tile in the complexity X artwork with another copy of the original sequence</li>
	<li>replace each <code>G</code> tile in the complexity X artwork with K <code>G</code> tiles</li>
</ul>

<p>For example, for an original sequence of <code>LGL</code>, the pieces of artwork with complexity 1 through 3 are:</p>

<ul>
	<li>C = 1: <code>LGL</code> (which is just the original sequence)</li>
	<li>C = 2: <code>LGLGGGLGL</code></li>
	<li>C = 3: <code>LGLGGGLGLGGGGGGGGGLGLGGGLGL</code></li>
</ul>

<p>Here's an illustration of how the artwork with complexity 2 is generated from the artwork with complexity 1:</p>

<p><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/14381/%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C.png"></p>

<p>You have just discovered a piece of Fractal artwork, but the tiles are too dirty for you to tell what they are made of. Because you are an expert archaeologist familiar with the local Fractal culture, you know the values of K and C for the artwork, but you do not know the original sequence. Since gold is exciting, you would like to know whether there is at least one <code>G</code> tile in the artwork. Your budget allows you to hire S graduate students, each of whom can clean one tile of your choice (out of the K<sup>C</sup> tiles in the artwork) to see whether the tile is <code>G</code> or <code>L</code>.</p>

<p>Is it possible for you to choose a set of no more than S specific tiles to clean, such that no matter what the original pattern was, you will be able to know for sure whether at least one <code>G</code> tile is present in the artwork? If so, which tiles should you clean?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with three integers: K, C, and S.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤ T ≤ 100.</li>
	<li>1 ≤ K ≤ 100.</li>
	<li>1 ≤ C ≤ 100.</li>
	<li>K<sup>C</sup> ≤ 10<sup>18</sup>.</li>
	<li>S = K.</li>
</ul>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is either <code>IMPOSSIBLE</code> if no set of tiles will answer your question, or a list of between 1 and S positive integers, which are the positions of the tiles that will answer your question. The tile positions are numbered from 1 for the leftmost tile to K<sup>C</sup> for the rightmost tile. Your chosen positions may be in any order, but they must all be different.</p>

