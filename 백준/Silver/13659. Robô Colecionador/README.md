# [Silver III] Robô Colecionador - 13659 

[문제 링크](https://www.acmicpc.net/problem/13659) 

### 성능 요약

메모리: 114004 KB, 시간: 176 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2024년 2월 5일 08:58:26

### 문제 설명

<p>Um dos esportes favoritos na Robolândia é o Rali dos Robôs. Este rali é praticado em uma arena retangular gigante de N linhas por M colunas de células quadradas. Algumas das células estão vazias, algumas contêm figurinhas da Copa (muito apreciadas pelas inteligências artificiais da Robolândia) e algumas são ocupadas por pilastras que sustentam o teto da arena. Em seu percurso os robôs podem ocupar qualquer célula da arena, exceto as que contém pilastras, que bloqueiam o seu movimento. O percurso do robô na arena durante o rali é determinado por uma sequência de instruções. Cada instrução é representada por um dos seguintes caracteres: ‘D’, ‘E’ e ‘F’, significando, respectivamente, “gire 90 graus para a direita”, “gire 90 graus para a esquerda” e “ande uma célula para a frente”. O robô começa o rali em uma posição inicial na arena e segue fielmente a sequência de instruções dada (afinal, eles são robôs!). Sempre que o robô ocupa uma célula que contém uma figurinha da Copa ele a coleta. As figurinhas da Copa não são repostas, ou seja, cada figurinha pode ser coletada uma unica vez. Quando um robô tenta andar para uma célula onde existe uma pilastra ele patina, permanecendo na célula onde estava, com a mesma orientação. O mesmo também acontece quando um robô tenta sair da arena.</p>

<p>Dados o mapa da arena, descrevendo a posição de pilastras e figurinhas, e a sequência de instruções de um robô, você deve escrever um programa para determinar o número de figurinhas coletadas pelo robô.</p>

### 입력 

 <p>A entrada contém vários casos de teste. A primeira linha de um caso de teste contém três números inteiros N, M e S (1 ≤ N, M ≤ 100, 1 ≤ S ≤ 5 × 10<sup>4</sup>), separados por espaços em branco, indicando respectivamente o número de linhas e o número de colunas da arena e o número de instruções para o robô. Cada uma das N linhas seguintes da entrada descreve uma linha de células da arena e contém uma cadeia com M caracteres. A primeira linha que aparece na descrição da arena é a que está mais ao Norte; a primeira coluna que aparece na descrição de uma linha de células da arena é a que está mais a Oeste.</p>

<p>Cada célula da arena pode conter um dos seguintes caracteres:</p>

<ul>
	<li>‘.’ — célula normal;</li>
	<li>‘*’ — célula que contém uma figurinha da Copa;</li>
	<li>‘#’ — célula que contém uma pilastra;</li>
	<li>‘N’, ‘S’, ‘L’, ‘O’ — célula onde o robô inicia o percurso (única na arena). A letra representa a orientação inicial do robô (Norte, Sul, Leste e Oeste, respectivamente).</li>
</ul>

<p>A ultima linha da entrada contém uma sequência de S caracteres dentre ‘D’, ‘E’ e ‘F’, representando as instruções do robô.</p>

<p>O último caso de teste é seguido por uma linha que contém apenas três números zero separados por um espaço em branco.</p>

### 출력 

 <p>Para cada rali descrito na entrada seu programa deve imprimir uma única linha contendo um único inteiro, indicando o número de figurinhas que o robô colecionou durante o rali.</p>

