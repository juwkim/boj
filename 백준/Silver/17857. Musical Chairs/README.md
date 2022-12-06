# [Silver V] Musical Chairs - 17857 

[문제 링크](https://www.acmicpc.net/problem/17857) 

### 성능 요약

메모리: 32424 KB, 시간: 104 ms

### 분류

자료 구조(data_structures), 구현(implementation), 큐(queue), 시뮬레이션(simulation)

### 문제 설명

<p>Professor O’Dagio of the music department at Faber College has come up with a rather interesting way of selecting its department chair. All n members of the music faculty line up, then the first one in line calls out an integer k corresponding to the opus number of his or her favorite musical composition by Faber College’s most illustrious alumnus, composer I. M. Tondeff. The department members then “count off,” starting with the first in line and cycling back to the beginning of the line if necessary. When the count reaches k, that person steps out of the line and is relieved (in more than one sense!) of chairmanship duty for that year.</p>

<p>The next person in line then calls out his or her favorite opus number (this becomes the new value of k) and the count restarts at “1,” and continues until the next person is eliminated, and so on. When only one faculty member is left standing, this is the new department chair. To prevent cheating, everyone’s favorite number is announced in advance and no one is allowed to choose Tondeff’s Opus 1 (the famous drinking song Rhapsody in Brew).</p>

<p>For instance, suppose the professors are numbered 1 through 4 and lined up in that order; suppose their favorite opus numbers are, respectively, opus 8 (The Four Sneezings), opus 2 (Concerto for Kazoo and Cigar Box Banjo), opus 4 (The Taekwondo Rondo), and opus 2 (again). Figure F.1 shows the process by which the new chair is selected.</p>

<table class="table table-bordered" style="width:100%;">
	<tbody>
		<tr>
			<td><code>(1)  (2)  (3)  (4)</code><br>
			<code> 8    2    4    2</code></td>
			<td style="vertical-align:middle;">Professor (1) calls out “8” and begins counting</td>
		</tr>
		<tr>
			<td><code>(1)  (2)  (3)     </code><br>
			<code> 8    2    4     </code></td>
			<td style="vertical-align:middle;">Professor (4) is eliminated. Professor (1) (the next in line) calls out “8” and begins counting</td>
		</tr>
		<tr>
			<td><code>(1)       (3)     </code><br>
			<code> 8         4     </code></td>
			<td style="vertical-align:middle;">Professor (2) is eliminated. Professor (3) (the next in line) calls out “4” and begins counting</td>
		</tr>
		<tr>
			<td><code>          (3)     </code><br>
			<code>           4     </code></td>
			<td style="vertical-align:middle;">Professor (1) is eliminated. Professor (3) is the new department chair</td>
		</tr>
	</tbody>
</table>

<p style="text-align: center;">Figure F.1: Example of Selection Process</p>

### 입력 

 <p>The first line of input contains an integer n (2 ≤ n ≤ 10<sup>4</sup>), the number of faculty members. The next line contains n integers k<sub>1</sub> . . . k<sub>n</sub> (2 ≤ k<sub>i</sub> ≤ 10<sup>6</sup> for each i), where ki is the favorite opus number of professor i.</p>

### 출력 

 <p>Output the number of the new department chair.</p>

