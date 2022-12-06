# [Bronze II] Jogo de Estratégia - 13604 

[문제 링크](https://www.acmicpc.net/problem/13604) 

### 성능 요약

메모리: 48788 KB, 시간: 116 ms

### 분류

구현(implementation)

### 문제 설명

<p>Um jogo de estratégia, com J jogadores, é jogado em volta de uma mesa. O primeiro a jogar é o jogador 1, o segundo a jogar é o jogador 2 e assim por diante. Uma vez completada uma rodada, novamente o jogador 1 faz sua jogada e a ordem dos jogadores se repete novamente. A cada jogada, um jogador garante uma certa quantidade de Pontos de Vitória. A pontuação de cada jogador consiste na soma dos Pontos de Vitória de cada uma das suas jogadas.</p>

<p>Dado o número de jogadores, o número de rodadas e uma lista representando os Pontos de Vitória na ordem em que foram obtidos, você deve determinar qual é o jogador vencedor. Caso mais de um jogador obtenha a pontuação máxima, o jogador com pontuação máxima que tiver jogado por último é o vencedor.</p>

### 입력 

 <p>A entrada consiste de duas linhas. A primeira linha contém dois inteiros J e R, o número de jogadores e de rodadas respectivamente (1 ≤ J, R ≤ 500). A segunda linha contém J × R inteiros, correspondentes aos Pontos de Vitória em cada uma das jogadas feitas, na ordem em que aconteceram. Os Pontos de Vitória obtidos em cada jogada serão sempre inteiros entre 0 e 100, inclusive.</p>

### 출력 

 <p>Seu programa deve produzir uma única linha, contendo o inteiro correspondente ao jogador vencedor.</p>

