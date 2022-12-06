# [Bronze I] Dominant Species - 10175 

[문제 링크](https://www.acmicpc.net/problem/10175) 

### 성능 요약

메모리: 31856 KB, 시간: 92 ms

### 분류

구현(implementation)

### 문제 설명

<p>The Natural Wildlife Federation is trying to determine the dominant species in several different areas in the United States. They have sent researchers out to record the current population of four different predators (Bobcat, Coyote, Mountain Lion, and Wolf). They will use this information to determine which species dominates a particular ecological location. Because the animals differ in size, weight, and hunting ability each species has been given a weighted value as follows:</p>

<table class="table table-bordered" style="width:20%">
	<thead>
		<tr>
			<th>Species</th>
			<th>Value</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Bobcat</td>
			<td>2</td>
		</tr>
		<tr>
			<td>Coyote</td>
			<td>1</td>
		</tr>
		<tr>
			<td>Mountain Lion</td>
			<td>4</td>
		</tr>
		<tr>
			<td>Wolf</td>
			<td>3</td>
		</tr>
	</tbody>
</table>

<p>Thus, one Mountain Lion is equivalent to two Bobcats and one Wolf is equivalent to three Coyotes. The researchers have recorded animal sightings by writing a B for bobcat, C for coyote, M for mountain lion, and W for wolf. For example, if the researcher at Saguaro saw 5 wolves, 10 coyotes, 2 bobcats, and no mountain lions they might record this with the string “Saguaro WCCCBCCCCWWBCCWWC”</p>

<p>They need your help to process the raw data and determine the dominant species.</p>

### 입력 

 <p>The first line of input will be a positive integer, n, indicating the number of problem sets to follow. Each problem set is comprised of one line of text. Each line will contain two “words”. The first word will be the location and the second word will be the species count as described above. The second word will have no blanks and only contain the letters ‘B’, ‘C’, ‘M’, and ‘W’. The length of word does not exceed 100.</p>

### 출력 

 <p>For each problem set print one of the two followings statements:</p>

<pre><x>: The <y> is the dominant species
<x>: There is no dominant species</pre>

<p>In the lines above the place holder <x> should be replaced with the location, and the place holder <y> should be replace with either Bobcat, Coyote, Mountain Lion, or Wolf, where the species selected is the dominant species.</p>

