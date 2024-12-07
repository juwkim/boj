# [Silver II] 맹세 - 3407 

[문제 링크](https://www.acmicpc.net/problem/3407) 

### 성능 요약

메모리: 116904 KB, 시간: 344 ms

### 분류

브루트포스 알고리즘, 다이나믹 프로그래밍, 그래프 이론, 그래프 탐색, 문자열

### 제출 일자

2024년 12월 8일 02:23:27

### 문제 설명

<p>위대한 화학자 김선영은 그를 바라보며 굳은 맹세를 했다.</p>

<blockquote>난 오늘부터 원소 기호로 이루어진 단어만을 말할 것이다.</blockquote>

<p>선영이는 "I Am CLaRa"를 말할 수 있다. I 는 아이오딘, Am은 아메리슘, C는 탄소, La는 란타넘, Ra는 라듐이다. 또, 선영이는 "InTeRnAtIONAl"도 말할 수 있다. 하지만, "collegiate", "programming", "contest"는 원소 기호로 이루어진 단어가 아니기 때문에 말할 수 없다.</p>

<p>단어가 주어졌을 때, 선영이가 말할 수 있는 단어 인지 (원소 기호가 연결된 단어) 아닌지를 구하는 프로그램을 작성하시오. (대소문자는 가리지 않는다)</p>

<p>다음은 이 문제에서 사용하는 원소 주기율표이다.</p>

<table class="table table-bordered">
	<tbody>
		<tr>
			<td>H</td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td>He</td>
		</tr>
		<tr>
			<td>Li</td>
			<td>Be</td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td>B</td>
			<td>C</td>
			<td>N</td>
			<td>O</td>
			<td>F</td>
			<td>Ne</td>
		</tr>
		<tr>
			<td>Na</td>
			<td>Mg</td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td> </td>
			<td>Al</td>
			<td>Si</td>
			<td>P</td>
			<td>S</td>
			<td>Cl</td>
			<td>Ar</td>
		</tr>
		<tr>
			<td>K</td>
			<td>Ca</td>
			<td>Sc</td>
			<td>Ti</td>
			<td>V</td>
			<td>Cr</td>
			<td>Mn</td>
			<td>Fe</td>
			<td>Co</td>
			<td>Ni</td>
			<td>Cu</td>
			<td>Zn</td>
			<td>Ga</td>
			<td>Ge</td>
			<td>As</td>
			<td>Se</td>
			<td>Br</td>
			<td>Kr</td>
		</tr>
		<tr>
			<td>Rb</td>
			<td>Sr</td>
			<td>Y</td>
			<td>Zr</td>
			<td>Nb</td>
			<td>Mo</td>
			<td>Tc</td>
			<td>Ru</td>
			<td>Rh</td>
			<td>Pd</td>
			<td>Ag</td>
			<td>Cd</td>
			<td>In</td>
			<td>Sn</td>
			<td>Sb</td>
			<td>Te</td>
			<td>I</td>
			<td>Xe</td>
		</tr>
		<tr>
			<td>Cs</td>
			<td>Ba</td>
			<td>*</td>
			<td>Hf</td>
			<td>Ta</td>
			<td>W</td>
			<td>Re</td>
			<td>Os</td>
			<td>Ir</td>
			<td>Pt</td>
			<td>Au</td>
			<td>Hg</td>
			<td>Tl</td>
			<td>Pb</td>
			<td>Bi</td>
			<td>Po</td>
			<td>At</td>
			<td>Rn</td>
		</tr>
		<tr>
			<td>Fr</td>
			<td>Ra</td>
			<td>**</td>
			<td>Rf</td>
			<td>Db</td>
			<td>Sg</td>
			<td>Bh</td>
			<td>Hs</td>
			<td>Mt</td>
			<td>Ds</td>
			<td>Rg</td>
			<td>Cn</td>
			<td> </td>
			<td>Fl</td>
			<td> </td>
			<td>Lv</td>
			<td> </td>
			<td> </td>
		</tr>
		<tr>
			<td colspan="3">* 란타넘족</td>
			<td>La</td>
			<td>Ce</td>
			<td>Pr</td>
			<td>Nd</td>
			<td>Pm</td>
			<td>Sm</td>
			<td>Eu</td>
			<td>Gd</td>
			<td>Tb</td>
			<td>Dy</td>
			<td>Ho</td>
			<td>Er</td>
			<td>Tm</td>
			<td>Yb</td>
			<td>Lu</td>
		</tr>
		<tr>
			<td colspan="3">** 악티늄족</td>
			<td>Ac</td>
			<td>Th</td>
			<td>Pa</td>
			<td>U</td>
			<td>Np</td>
			<td>Pu</td>
			<td>Am</td>
			<td>Cm</td>
			<td>Bk</td>
			<td>Cf</td>
			<td>Es</td>
			<td>Fm</td>
			<td>Md</td>
			<td>No</td>
			<td>Lr</td>
		</tr>
	</tbody>
</table>

### 입력 

 <p>첫째 줄에 테스트 케이스의 개수 T가 주어진다. 다음 T개의 줄에는 알파벳 소문자로만 된 단어가 하나 주어진다. 단어의 길이는 50,000을 넘지 않으며 양수이다.</p>

### 출력 

 <p>입력으로 주어진 단어가 선영이가 발음할 수 있는 단어라면 YES를, 아니라면 NO를 출력한다.</p>

