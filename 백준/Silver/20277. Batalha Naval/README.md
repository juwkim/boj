# [Silver V] Batalha Naval - 20277 

[문제 링크](https://www.acmicpc.net/problem/20277) 

### 성능 요약

메모리: 113112 KB, 시간: 120 ms

### 분류

구현(implementation)

### 문제 설명

<p>Batalha Naval é um clássico jogo de estratégia para dois jogadores. Cada jogador posiciona seus navios num grid 10 × 10, e cada rodada do jogo consiste em adivinhar as posições dos navios do adversário. Existem muitas variações das regras, mas tais regras são irrelevantes para esse problema. Estamos interessados num problema mais básico: Dada a lista dos navios e suas posições, você deve determinar se o posicionamento inicial é válido.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 330px; height: 327px;"></p>

<p>As linhas e colunas do tabuleiro são numeradas de 1 a 10, e os navios são posicionados na horizontal ou na vertical, ocupando uma sequência contígua de quadrados do tabuleiro. Para esse problema, um posicionamento é válido se:</p>

<ul>
	<li>nenhuma posição é ocupada por mais de um navio e;</li>
	<li>todos os navios estão inteiramente contidos no tabuleiro.</li>
</ul>

### 입력 

 <p>A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 100), o número de navios. Cada uma das próximas N linhas contém quatro inteiros D, L, R e C com D ∈ {0, 1}, 1 ≤ L ≤ 5 e 1 ≤ R, C ≤ 10 descrevendo um navio. Se D = 0 então o navio está alinhado horizontalmente, e ocupa as posições (R, C). . .(R, C + L − 1). Do contrário, o navio está alinhado verticalmente, e ocupa as posições (R, C). . .(R + L − 1, C).</p>

### 출력 

 <p>Imprima uma única linha contendo um único caractere. Se o posicionamento inicial dos navios for válido, então imprima o caractere maiúsculo ‘Y’; do contrário, imprima o caractere maiúsculo ‘N’.</p>

