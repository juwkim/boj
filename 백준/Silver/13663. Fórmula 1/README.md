# [Silver III] Fórmula 1 - 13663 

[문제 링크](https://www.acmicpc.net/problem/13663) 

### 성능 요약

메모리: 110432 KB, 시간: 116 ms

### 분류

구현, 시뮬레이션, 정렬

### 제출 일자

2024년 12월 4일 19:17:53

### 문제 설명

<p>A temporada de Fórmula 1 consiste de uma série de corridas, conhecidas como Grandes Prêmios, organizados pela Federação Internacional de Automobilismo (FIA). Os resultados de cada Grande Prêmio são combinados para determinar o Campeonato Mundial de Pilotos. Mais especificamente, a cada Grande Prêmio são distribuídos pontos para os pilotos, dependendo da classificação na corrida. Ao final da temporada, o piloto que tiver somado o maior número de pontos é declarado Campeão Mundial de Pilotos.<br>
<br>
Os organizadores da Fórmula 1 mudam constantemente as regras da competição, com o objetivo de dar mais emoção às disputas. Uma regra modificada para a temporada de 2010 foi justamente a distribuição de pontos em cada Grande Prêmio. Desde 2003 a regra de pontuação premiava os oito primeiros colocados, obedecendo a seguinte tabela:</p>

<table border="1" cellpadding="1" cellspacing="1" style="width:300px">
	<tbody>
		<tr>
			<td>Colocação</td>
			<td>1</td>
			<td>2</td>
			<td>3</td>
			<td>4</td>
			<td>5</td>
			<td>6</td>
			<td>7</td>
			<td>8</td>
		</tr>
		<tr>
			<td>Pontos</td>
			<td>10</td>
			<td>8</td>
			<td>6</td>
			<td>5</td>
			<td>4</td>
			<td>3</td>
			<td>2</td>
			<td>1</td>
		</tr>
	</tbody>
</table>

<p>Ou seja, o piloto vencedor ganhava 10 pontos, o segundo colocado ganhava 8 pontos, e assim por diante.</p>

<p>Na temporada de 2010, os dez primeiros colocados receberão pontos obedecendo a seguinte tabela:</p>

<table border="1" cellpadding="1" cellspacing="1" style="width:300px">
	<tbody>
		<tr>
			<td>Colocação</td>
			<td>1</td>
			<td>2</td>
			<td>3</td>
			<td>4</td>
			<td>5</td>
			<td>6</td>
			<td>7</td>
			<td>8</td>
			<td>9</td>
			<td>10</td>
		</tr>
		<tr>
			<td>Pontos</td>
			<td>25</td>
			<td>18</td>
			<td>15</td>
			<td>12</td>
			<td>10</td>
			<td>8</td>
			<td>6</td>
			<td>4</td>
			<td>2</td>
			<td>1</td>
		</tr>
	</tbody>
</table>

<p>A mudança no sistema de pontuação provocou muita especulação sobre qual teria sido o efeito nos Campeonatos Mundiais passados se a nova pontuação tivesse sido utilizada nas temporadas anteriores. Por exemplo, teria Lewis Hamilton sido campeão em 2008, já que a diferença de sua pontuação total para Felipe Massa foi de apenas um ponto? Para acabar com as especulações, a FIA contratou você para escrever um programa que, dados os resultados de cada corrida de uma temporada determine Campeão Mundial de Pilotos para sistemas de pontuações diferentes.</p>

### 입력 

 <p>A entrada contém vários casos de teste. A primeira linha de um caso de teste contém dois números inteiros G e P separados por um espaço em branco, indicando respectivamente o número de Grandes Prêmios (1 ≤ G ≤ 100) e o número de pilotos (1 ≤ P ≤ 100). Os pilotos são identificados por inteiros de 1 a P. Cada uma das G linhas seguintes indica o resultado de uma corrida, e contém P inteiros separados por espaços em branco. Em cada linha, o i-ésimo número indica a ordem de chegada do pilodo i na corrida (o primeiro número indica a ordem de chegada do piloto 1 naquela corrida, o segundo número indica a ordem de chegada do piloto 2 na corrida, e assim por diante). A linha seguinte contém um único número inteiro S indicando o número de sistemas de pontuação (1 ≤ S ≤ 10), e após, cada uma das S linhas seguintes contém a descrição de um sistema de pontuação. A descrição de um sistema de pontuação inicia com um inteiro K (1 ≤ K ≤ P), indicando a última ordem de chegada que receberá pontos, seguido de um espaço em branco, seguido de K inteiros k<sub>0</sub>, k<sub>1</sub>, ... , k<sub>n−1</sub> (1 ≤ k<sub>i</sub> ≤ 100) separados por espaços em branco, indicando os pontos a serem atribuídos (o primeiro inteiro indica os pontos do primeiro colocado, o segundo inteiro indica os pontos do segundo colocado, e assim por diante).</p>

<p>O último caso de teste é seguido por uma linha que contém apenas dois números zero separados por um espaço em branco.</p>

### 출력 

 <p>Para cada caso de sistema de pontuação da entrada seu programa deve imprimir uma linha, que deve conter o identificador do Campeão Mundial de Pilotos. Se houver mais de um Campeão Mundial Pilotos (ou seja, se houver empate), a linha deve conter todos os Campeões Mundiais de Pilotos, em ordem crescente de identificador, separados por um espaço em branco.</p>

