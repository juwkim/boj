# [Silver V] Semmy - 26508 

[문제 링크](https://www.acmicpc.net/problem/26508) 

### 성능 요약

메모리: 113112 KB, 시간: 112 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>In the semaphore signaling system, two flags are held, one in each hand, with arms extended, in various positions representing the letters of the alphabet. The pattern resembles a compass rose divided into eight positions: up (U), down (D), out (O), high (H) and low (L), for each hand. The left hand signal is always read first. Additionally, six letters require a hand to be brought across the body so that both flags are on the same side. As an example the letter H has the left hand across the body and held low (AL).</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/53297d99-3eec-4e38-b373-e650844e8fdb/-/preview/" style="width: 461px; height: 168px;"></p>

<table class="table table-bordered th-center td-center table-center-40">
	<thead>
		<tr>
			<th>ALPHA</th>
			<th>LEFT</th>
			<th>RIGHT</th>
			<th>ALPHA</th>
			<th>LEFT</th>
			<th>RIGHT</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>A</td>
			<td>D</td>
			<td>L</td>
			<td>N</td>
			<td>L</td>
			<td>L</td>
		</tr>
		<tr>
			<td>B</td>
			<td>D</td>
			<td>O</td>
			<td>O</td>
			<td>AH</td>
			<td>O</td>
		</tr>
		<tr>
			<td>C</td>
			<td>D</td>
			<td>H</td>
			<td>P</td>
			<td>U</td>
			<td>O</td>
		</tr>
		<tr>
			<td>D</td>
			<td>D</td>
			<td>U</td>
			<td>Q</td>
			<td>H</td>
			<td>O</td>
		</tr>
		<tr>
			<td>E</td>
			<td>H</td>
			<td>D</td>
			<td>R</td>
			<td>O</td>
			<td>O</td>
		</tr>
		<tr>
			<td>F</td>
			<td>O</td>
			<td>D</td>
			<td>S</td>
			<td>L</td>
			<td>O</td>
		</tr>
		<tr>
			<td>G</td>
			<td>L</td>
			<td>D</td>
			<td>T</td>
			<td>U</td>
			<td>H</td>
		</tr>
		<tr>
			<td>H</td>
			<td>AL</td>
			<td>O</td>
			<td>U</td>
			<td>H</td>
			<td>H</td>
		</tr>
		<tr>
			<td>I</td>
			<td>AL</td>
			<td>U</td>
			<td>V</td>
			<td>L</td>
			<td>U</td>
		</tr>
		<tr>
			<td>J</td>
			<td>O</td>
			<td>U</td>
			<td>W</td>
			<td>O</td>
			<td>AH</td>
		</tr>
		<tr>
			<td>K</td>
			<td>U</td>
			<td>L</td>
			<td>X</td>
			<td>L</td>
			<td>AH</td>
		</tr>
		<tr>
			<td>L</td>
			<td>H</td>
			<td>L</td>
			<td>Y</td>
			<td>O</td>
			<td>H</td>
		</tr>
		<tr>
			<td>M</td>
			<td>O</td>
			<td>L</td>
			<td>Z</td>
			<td>O</td>
			<td>AL</td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>A data file that contains all letter/signal combinations on the first 26 lines, followed by two sets of data, each starting with an integer N. The first group contains N coded expressions that represent words or phrases, and the second group contains N English words or phrases. In the first group, a # indicates a space between words.</p>

### 출력 

 <p>Decode the first group of coded signal expressions into the English word or phrase, and encode the second group into the appropriate signal expression, with any spaces between words represented by the # sign.</p>

