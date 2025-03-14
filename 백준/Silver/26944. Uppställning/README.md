# [Silver II] Uppställning - 26944 

[문제 링크](https://www.acmicpc.net/problem/26944) 

### 성능 요약

메모리: 113836 KB, 시간: 240 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2025년 3월 15일 00:53:39

### 문제 설명

<p>En grupp med n barn, låt oss kalla dem A, B, C och så vidare, beslutar sig för att testa din tankeförmåga. Utan att du ser dem ställer de upp sig på en rad. Sen räknar vart och en av dem hur många av de barn som står till vänster som är längre än hen själv, och sedan likadant med dem som står till höger. Var och en skriver ner dessa antal på en lapp som de ger till dig efter att ha frångått uppställningen. Deras enkla uppmaning till dig är att tala om i vilken ordning de stod.</p>

<p>Ett exempel med fem barn visas i figuren. A har ett längre barn (D) till vänster om sig och två (C och E) till höger. B har tre längre barn till vänster om sig och ett till höger. C har ett längre barn till vänster om sig men inget till höger och så vidare. Informationen på lapparna kan sammanfattas så här:</p>

<table class="table table-bordered table-center-20">
	<tbody>
		<tr>
			<th>Barn</th>
			<th>Vänster</th>
			<th>Höger</th>
		</tr>
		<tr>
			<td>A</td>
			<td>1</td>
			<td>2</td>
		</tr>
		<tr>
			<td>B</td>
			<td>3</td>
			<td>1</td>
		</tr>
		<tr>
			<td>C</td>
			<td>1</td>
			<td>0</td>
		</tr>
		<tr>
			<td>D</td>
			<td>0</td>
			<td>0</td>
		</tr>
		<tr>
			<td>E</td>
			<td>2</td>
			<td>0</td>
		</tr>
	</tbody>
</table>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/1f9dda4e-60b2-4c40-a5cf-4ac20dc1b3e3/-/preview/" style="width: 144px; height: 117px;"></p>

<p>Tyvärr klarade du inte nöten utan måste i hemlighet smyga iväg och skriva ett datorprogram som löser uppgiften. För att underlätta för dig själv nästa gång barnen ansätter dig så vill du kunna variera både antalet barn (mellan 3 och 8, inklusive) och informationen på lapparna. Du kan förutsätta att alla barn är olika långa och att de inte har gjort något misstag när de skrev lapparna. Intressant nog finns det aldrig mer än en lösning.</p>

### 입력 

 <p>Första raden i indata består av ett heltal <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c38"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>8</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3 \le n \le 8$</span></mjx-container>), antal barn. Därefter följer <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> rader med två heltal vardera: antal barn till vänster som är längre än barnet självt, och antalet till höger.</p>

### 출력 

 <p>Skriv ut en rad med <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> tecken som beskriver barnens uppställning, som en omkastning av bokstäverna <code>A</code>, <code>B</code>, <code>C</code>, etc.</p>

