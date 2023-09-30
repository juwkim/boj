# [Silver IV] Automatic Editing - 4668 

[문제 링크](https://www.acmicpc.net/problem/4668) 

### 성능 요약

메모리: 113112 KB, 시간: 112 ms

### 분류

구현, 문자열

### 문제 설명

<p>Text-processing tools like awk and sed allow you to automatically perform a sequence of editing operations based on a script. For this problem we consider the specific case in which we want to perform a series of string replacements, within a single line of text, based on a fixed set of rules. Each rule specifies the string to find, and the string to replace it with, as shown below.</p>

<table class="table-bordered table" style="width-50%;">
	<tbody>
		<tr>
			<td style="text-align:center">Rule</td>
			<td style="text-align:center">Find</td>
			<td style="text-align:center">Replace-by</td>
		</tr>
		<tr>
			<td style="text-align:right">1.</td>
			<td>ban</td>
			<td>bab</td>
		</tr>
		<tr>
			<td style="text-align:right">2.</td>
			<td>baba</td>
			<td>be</td>
		</tr>
		<tr>
			<td style="text-align:right">3.</td>
			<td>ana</td>
			<td>any</td>
		</tr>
		<tr>
			<td style="text-align:right">4.</td>
			<td>ba b</td>
			<td>hind the g</td>
		</tr>
	</tbody>
</table>

<p>To perform the edits for a given line of text, start with the first rule. Replace the first occurrence of the find string within the text by the replace-by string, then try to perform the same replacement again on the new text. Continue until the find string no longer occurs within the text, and then move on to the next rule. Continue until all the rules have been considered. Note that (1) when searching for a find string, you always start searching at the beginning of the text, (2) once you have finished using a rule (because the find string no longer occurs) you never use that rule again, and (3) case is significant.</p>

<p>For example, suppose we start with the line</p>

<p style="margin-left:40px">banana boat</p>

<p>and apply these rules. The sequence of transformations is shown below, where occurrences of a find string are underlined and replacements are boldfaced. Note that rule 1 was used twice, then rule 2 was used once, then rule 3 was used zero times, and then rule 4 was used once.</p>

<table class="table-bordered table" style="width-50%;">
	<tbody>
		<tr>
			<td>Before</td>
			<td>After</td>
		</tr>
		<tr>
			<td><u>ban</u>ana boat</td>
			<td><strong>bab</strong>ana boat</td>
		</tr>
		<tr>
			<td>ba<u>ban</u>a boat</td>
			<td>ba<strong>bab</strong>a boat</td>
		</tr>
		<tr>
			<td><u>baba</u>ba boat</td>
			<td><strong>be</strong>ba boat</td>
		</tr>
		<tr>
			<td>be<u>ba bo</u>at</td>
			<td>be<strong>hind the g</strong>oat</td>
		</tr>
	</tbody>
</table>

<p> </p>

### 입력 

 <p>The input contains one or more test cases, followed by a line containing only 0 (zero) that signals the end of the file. Each test case begins with a line containing the number of rules, which will be between 1 and 10. Each rule is specified by a pair of lines, where the first line is the find string and the second line is the replace-by string. Following all the rules is a line containing the text to edit.</p>

### 출력 

 <p>For each test case, output a line containing the final edited text.</p>

<p> </p>

