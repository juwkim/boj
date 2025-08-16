# [Silver I] Rouba-Monte - 13578 

[문제 링크](https://www.acmicpc.net/problem/13578) 

### 성능 요약

메모리: 110932 KB, 시간: 108 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 8월 16일 18:17:06

### 문제 설명

<p>Um dos jogos de cartas mais divertidos para crianças pequenas, pela simplicidade, é Rouba- Monte. O jogo utiliza um ou mais baralhos normais e tem regras muito simples. Cartas são distingüidas apenas pelo valor (ás, dois, três, . . .), ou seja, os naipes das cartas não são considerados (por exemplo, ás de paus e ás de ouro têm o mesmo valor).</p>

<p>Inicialmente as cartas são embaralhadas e colocadas em uma pilha na mesa de jogo, chamada de pilha de compra, com face voltada para baixo. Durante o jogo, cada jogador mantém um <em>monte</em> de cartas, com face voltada para cima; em um dado momento o monte de um jogador pode conter zero ou mais cartas. No início do jogo, todos os montes dos jogadores têm zero cartas. Ao lado da pilha de compras encontra-se uma área denomindada de <em>área de descarte</em>, inicialmente vazia, e todas as cartas colocadas na área de descarte são colocadas lado a lado com a face para cima (ou seja, não são empilhadas).</p>

<p>Os jogadores, dispostos em um círculo ao redor da mesa de jogo, jogam em sequência, em sentido horário. As jogadas prosseguem da seguinte forma:</p>

<ul>
	<li>O jogador que tem a vez de jogar retira a carta de cima da pilha de compras e a mostra aos outros jogadores; vamos chamar essa carta de <em>carta da vez</em>.</li>
	<li>Se a carta da vez for igual a alguma carta presente na área de descarte, o jogador retira essa carta da área de descarte colocando-a, juntamente com a carta da vez, no topo de seu monte, com as faces voltada para cima, e continua a jogada (ou seja, retira outra carta da pilha de compras e repete o processo).</li>
	<li>Se a carta da vez for igual à carta de cima de um monte de um outro jogador, o jogador "rouba" esse monte, empilhando-o em seu próprio monte, coloca a carta da vez no topo do seu monte, face para cima, e continua a jogada.</li>
	<li>Se a carta da vez for igual à carta no topo de seu próprio monte, o jogador coloca a carta da vez no topo de seu próprio monte, com a face para cima, e continua a jogada.</li>
	<li>Se a carta da vez for diferente das cartas da área de descarte e das cartas nos topos dos montes, o jogador a coloca na área de descarte, face para cima, e a jogada se encerra (ou seja, o próximo jogador efetua a sua jogada). Note que esse é o único caso em que o jogador não continua a jogada.</li>
</ul>

<p>O jogo termina quando não há mais cartas na pilha de compras. O jogador que tiver o maior monte (o monte contendo o maior número de cartas) ganha o jogo. Se houver empate, todos os jogadores com o monte contendo o maior número de cartas ganham o jogo.</p>

### 입력 

 <p>A entrada é composta de vários casos de teste. A primeira linha de um caso de teste contém dois inteiros N e J, representando respectivamente o número de cartas no baralho (2 ≤ N ≤ 10.000) e o número de jogadores (2 ≤ J ≤ 20 e J ≤ N). As cartas do baralho são representadas por números inteiros de 1 a 13e os jogadores são identificados por inteiros de 1 a J. O primeiro jogador a jogar é o de número 1, seguido no jogador de número 2, . . ., seguido pelo jogador de número J, seguido pelo jogador de número 1, seguido do jogador de número 2, e assim por diante enquanto houver cartas na pilha de compras. A segunda linha de um caso de teste contém N inteiros entre 1 e 13, separados por um espaço em branco, representando as cartas na pilha de compras. As cartas são retiradas da pilha de compras na ordem em que aparecem na entrada. O final da entrada é indicado por uma linha com N = J = 0.</p>

### 출력 

 <p>Para cada caso de teste seu programa deve imprimir uma linha, contendo o número de cartas do monte do jogador ou jogadores que ganharam a partida, seguido de um espaço em branco, seguido do(s) identificador(es) dos jogadores que ganharam a partida. Se há mais de um jogador vencedor imprima os identificadores dos jogadores em ordem crescente, separados por um espaço em branco.</p>

