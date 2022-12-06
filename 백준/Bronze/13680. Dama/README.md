# [Bronze I] Dama - 13680 

[문제 링크](https://www.acmicpc.net/problem/13680) 

### 성능 요약

메모리: 30840 KB, 시간: 424 ms

### 분류

애드 혹(ad_hoc), 구현(implementation)

### 문제 설명

<p>O jogo de xadrez possui várias peças com movimentos curiosos: uma delas é a <em>dama</em>, que pode se mover qualquer quantidade de casas na mesma linha, na mesma coluna, ou em uma das duas diagonais, conforme exemplifica a figura abaixo:</p>

<p><img alt="" src="" style="height:175px; width:176px"></p>

<p>O grande mestre de xadrez Kary Gasparov inventou um novo tipo de problema de xadrez: dada a posição de uma dama em um tabuleiro de xadrez vazio (ou seja, um tabuleiro 8 × 8, com 64 casas), de quantos movimentos, no mínimo, ela precisa para chegar em outra casa do tabuleiro?</p>

<p>Kary achou a solução para alguns desses problemas, mas teve dificuldade com outros, e por isso pediu que você escrevesse um programa que resolve esse tipo de problema.  </p>

### 입력 

 <p>A entrada contém vários casos de teste. A primeira e única linha de cada caso de teste contém quatro inteiros X<sub>1</sub>, Y<sub>1</sub>, X<sub>2</sub> eY<sub>2</sub> (1 ≤ X<sub>1</sub>, Y<sub>1</sub>, X<sub>2</sub>, Y<sub>2</sub> ≤ 8). A dama começa na casa de coordenadas (X<sub>1</sub>, Y<sub>1</sub>), e a casa de destino é a casa de coordenadas(X<sub>2</sub>, Y<sub>2</sub>). No tabuleiro, as colunas são numeradas da esquerda para a direita de 1 a 8 e as linhas de cima para baixo também de 1 a 8. As coordenadas de uma casa na linha X e coluna Y são (X, Y ).</p>

<p>O final da entrada é indicado por uma linha contendo quatro zeros.</p>

### 출력 

 <p>Para cada caso de teste da entrada seu programa deve imprimir uma única linha na saída, contendo um número inteiro, indicando o menor número de movimentos necessários para a dama chegar em sua casa de destino.</p>

