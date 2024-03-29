# [Silver IV] Interruptores - 16450 

[문제 링크](https://www.acmicpc.net/problem/16450) 

### 성능 요약

메모리: 119908 KB, 시간: 272 ms

### 분류

구현, 시뮬레이션

### 문제 설명

<p>No painel de controle de um grande anfiteatro existem N interruptores, numerados de 1 a N, que controlam as M lâmpadas do local, numeradas de 1 a M. Note que o número de interruptores e lâmpadas não é necessariamente o mesmo e isso acontece porque cada interruptor está associado a um conjunto de lâmpadas e não apenas a uma lâmpada. Quando um interruptor é acionado, o estado de cada uma das lâmpadas associadas a ele é invertido. Quer dizer, aquelas apagadas acendem e as acesas se apagam.</p>

<p>Algumas lâmpadas estão acesas inicialmente e o zelador do anfiteatro precisa apagar todas as lâmpadas. Ele começou tentando acionar interruptores aleatoriamente mas, como não estava conseguindo apagar todas as lâmpadas ao mesmo tempo, decidiu seguir uma seguinte estratégia fixa. Ele vai acionar os interruptores na sequência 1, 2, 3, . . . , N, 1, 2, 3, . . . ou seja, toda vez após acionar o interruptor de número N, ele recomeça a sequência a partir do interruptor 1. Ele pretende acionar interruptores, seguindo essa estratégia, até que todas as lâmpadas estejam apagadas ao mesmo tempo (momento em que ele para de acionar os interruptores). Será que essa estratégia vai funcionar?</p>

<p>Neste problema, dadas as lâmpadas acesas inicialmente e dados os conjuntos de lâmpadas que estão associados a cada interruptor, seu programa deve computar o número de vezes que o zelador vai acionar os interruptores. Caso a estratégia do zelador nunca apague todas as lâmpadas ao mesmo tempo, seu programa deve imprimir −1.</p>

### 입력 

 <p>A primeira linha contém dois inteiros N e M (1 ≤ N, M ≤ 1000) representando, respectivamente, o número de interruptores e o número de lâmpadas. A segunda linha contém um inteiro L (1 ≤ L ≤ M) seguido por L inteiros distintos X<sub>i</sub> (1 ≤ X<sub>i</sub> ≤ M), representando as lâmpadas acesas inicialmente. Cada uma das N linhas seguintes contém um inteiro K<sub>i</sub> (1 ≤ K<sub>i</sub> ≤ M) seguido por K<sub>i</sub> inteiros distintos Y<sub>i</sub> (1 ≤ Y<sub>i</sub> ≤ M), representando as lâmpadas associadas ao interruptor i (1 ≤ i ≤ N).</p>

### 출력 

 <p>Se programa deve produzir uma única linha contendo um inteiro representando o número de vezes que o zelador vai acionar os interruptores, seguindo a estratégia descrita, até todas as lâmpadas estarem apagadas ao mesmo tempo. Caso isso nunca vá acontecer, imprima −1.</p>

