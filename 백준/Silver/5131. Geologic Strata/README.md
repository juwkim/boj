# [Silver I] Geologic Strata - 5131 

[문제 링크](https://www.acmicpc.net/problem/5131) 

### 성능 요약

메모리: 110732 KB, 시간: 104 ms

### 분류

구현

### 제출 일자

2025년 8월 16일 10:45:46

### 문제 설명

<p>Time-traveling is finicky business. Occasionally you end up hundreds of millions of years away from when you intended. So as a time-traveling salesman, Tim often wants to verify that he’s landed near his target date. This is easy if he’s traveling forward in time, as there are always people around who he can ask. But traveling back in time is a different story. Humans haven’t been around for very long, much less been keeping track of time with calendars. For these cases of traveling far back in time, Tim would like to develop a new mechanism for validating what time he’s landed in.</p>

<p>One strategy would be to use geologic dating principles. By taking a core sample of earth from the place he lands, Tim can study the layers of sediment, called strata, each of which was created during a specific geologic period. Though it’s easy to differentiate one stratum from another, it’s impossible to say which geologic period a stratum corresponds to without additional evidence, due to local variations in climate and soil structure. This is where fossils come in. If a stratum contains a fossil, then the corresponding geologic time period is known, based on previous studies of fossil records and the fact that all members of a species existed during the same geologic period. So to verify the time he’s landed in, all Tim needs to know is whether the strata in the core sample are consistent with the target time that he entered in his time machine.</p>

### 입력 

 <p>The first line is the number K of input data sets, followed by the K data sets, each of the following form:</p>

<p>The first line contains three integers t, w, and d: Tim’s target time (in millions of years ago), and the width and depth of the core sample, where 0 ≤ t ≤ 3000 and 1 ≤ w, d ≤ 100. The next d lines each contain w characters and represent the core sample. Possible characters are digits (0 through 9) and capital letters (A through M). A digit represents sediment belonging to a particular stratum, where stratum 0 is the surface of the earth, and thus should match the geologic period of Tim’s target time. Stratum 1 is the layer below stratum 0, stratum 2 the layer below stratum 1, and so on. Fossils will always be represented by a single capital letter, which will be one of the labels in the following table.</p>

<table class="table table-bordered" style="width:50%">
	<thead>
		<tr>
			<th>Period</th>
			<th>Range (millions of years ago)</th>
			<th>Fossil Label</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>Quaternary</td>
			<td>0 to 3</td>
			<td>A</td>
		</tr>
		<tr>
			<td>Neogene</td>
			<td>4 to 23</td>
			<td>B</td>
		</tr>
		<tr>
			<td>Paleogene</td>
			<td>24 to 66</td>
			<td>C</td>
		</tr>
		<tr>
			<td>Cretaceous</td>
			<td>67 to 146</td>
			<td>D</td>
		</tr>
		<tr>
			<td>Jurassic</td>
			<td>147 to 200</td>
			<td>E</td>
		</tr>
		<tr>
			<td>Triassic</td>
			<td>201 to 251</td>
			<td>F</td>
		</tr>
		<tr>
			<td>Permian</td>
			<td>252 to 299</td>
			<td>G</td>
		</tr>
		<tr>
			<td>Carboniferous</td>
			<td>300 to 359</td>
			<td>H</td>
		</tr>
		<tr>
			<td>Devonian</td>
			<td>360 to 416</td>
			<td>I</td>
		</tr>
		<tr>
			<td>Silurian</td>
			<td>417 to 444</td>
			<td>J</td>
		</tr>
		<tr>
			<td>Ordovician</td>
			<td>445 to 488</td>
			<td>K</td>
		</tr>
		<tr>
			<td>Cambrian</td>
			<td>489 to 542</td>
			<td>L</td>
		</tr>
		<tr>
			<td>Precambrian</td>
			<td>543+</td>
			<td>M</td>
		</tr>
	</tbody>
</table>

<p>A fossil belongs to the stratum immediately surrounding it, including diagonals. If a fossil is surrounded by more than one kind of stratum (e.g. both 1 and 2), assume the fossil belongs to the stratum with the numerically lowest digit. No fossil will be completely surrounded by other fossils, and there will always be at least one fossil and at least one stratum in the core sample.</p>

### 출력 

 <p>For each data set, output “Data Set x:” on a line by itself, where x is its number. On the next line, output “Yes” if all fossils in the core sample are consistent with Tim’s target time. Output “No” otherwise. Each data set should be followed by a blank line.</p>

