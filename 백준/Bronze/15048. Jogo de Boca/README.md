# [Bronze II] Jogo de Boca - 15048 

[문제 링크](https://www.acmicpc.net/problem/15048) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

임의 정밀도 / 큰 수 연산(arbitrary_precision), 게임 이론(game_theory), 수학(math)

### 문제 설명

<p>Um jogo infantil, muito popular, é o 21 de boca. O jogo é jogado da seguinte forma: o primeiro jogador diz um número, n<sub>0</sub>, que pode ser 1 ou 2. O segundo jogador pode então dizer um número n<sub>1</sub> tal que n<sub>1</sub> ∈ {n<sub>0</sub> + 1, n<sub>0</sub> + 2}. E assim por diante, os jogadores se alternam, dizendo sempre um número que é um ou dois maior do que o anterior. O jogador que disser 21 ganha o jogo. Por exemplo, a sequência de números poderia ser: 1, 3, 5, 6, 7, 9, 11, 12, 14, 15, 16, 18, 19, 21. Neste jogo, o primeiro jogador sempre perde, se o segundo souber jogar bem.</p>

<p>A cada nova geração as crianças ficam mais espertas. Atualmente, apesar de acharem o 21 de boca um jogo interessante, muitas crianças não se sentem desafiadas o bastante e por isso resolveram generalizar o jogo, criando assim o N de boca. Dado um inteiro N, no lugar do 21, o primeiro jogador pode escolher 1 ou 2. A partir daí os jogadores se alternam, adicionando 1 ou 2 ao número anterior, até que um deles diga o número N e ganhe o jogo. Sabendo que ambos os jogadores são excelentes e sabem jogar muito bem, seu problema é determinar qual o inteiro inicial que o primeiro jogador deve escolher para ganhar o jogo.</p>

### 입력 

 <p>A entrada consiste de uma única linha que contém o inteiro N (3 ≤ N ≤ 10<sup>100</sup>) escolhido para a partida atual do N de boca.</p>

### 출력 

 <p>Seu programa deve produzir uma única linha com um inteiro representando o número, em {1, 2}, que o primeiro jogador deve escolher, para ganhar o jogo. Se não for possível, então o inteiro deve ser zero.</p>

