# [Bronze I] Preludes - 23207 

[문제 링크](https://www.acmicpc.net/problem/23207) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Frederic Chopin was a Polish music composer who lived from 1810-1839. One of his most famous works was his set of preludes. These 24 pieces span the 24 musical keys (there are musically distinct 12 scale notes, and each may use major or minor tonality). The 12 distinct scale notes are:</p>

<table class="table table-bordered">
	<thead>
		<tr>
			<th>1</th>
			<th>2</th>
			<th>3</th>
			<th>4</th>
			<th>5</th>
			<th>6</th>
			<th>7</th>
			<th>8</th>
			<th>9</th>
			<th>10</th>
			<th>11</th>
			<th>12</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>A</td>
			<td>A♯ = B♭</td>
			<td>B</td>
			<td>C</td>
			<td>C♯ = D♭</td>
			<td>D</td>
			<td>D♯ = E♭</td>
			<td>E</td>
			<td>F</td>
			<td>F♯ = G♭</td>
			<td>G</td>
			<td>G♯ = A♭</td>
		</tr>
	</tbody>
</table>

<p>Five of the notes have two alternate names, as is indicated above with the equals sign (e.g. C♯ = D♭ means that note has two names, C♯ and D♭). Thus, there are 17 possible names for the scale notes, but only 12 musically distinct notes. When using one of these as the keynote for a musical key, we can further distinguish between the major and minor tonalities. This gives 34 possible keys, of which 24 are musically distinct.</p>

<p>In naming his preludes, Chopin used all the keys except for the following 10 (which were named instead by their alternate names):</p>

<p style="text-align: center;">A♭ minor A♯ major A♯ minor C♯ major D♭ minor D♯ major D♯ minor G♭ major G♭ minor G♯ major</p>

<p>Write a program that, given the name of a key, will give an alternate name (if it has an alternate) or report that the key name is unique.</p>

### 입력 

 <p>Each test case is described by one line of input having the format “<code>note tonality</code>”, where <code>note</code> is one of the 17 names for the scale notes given above, and <code>tonality</code> is either <code>major</code> or <code>minor</code>. All note names will be upper-case, and the two accidentals (♯ and ♭) will be written as <code>#</code> and <code>b</code>, respectively.</p>

### 출력 

 <p>For each case, display the case number followed by the alternate key name, if it exists, or print UNIQUE if the key name is unique. Follow the format of the sample output.</p>

