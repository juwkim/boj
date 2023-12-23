# [Silver IV] Cubos Coloridos - 13693 

[문제 링크](https://www.acmicpc.net/problem/13693) 

### 성능 요약

메모리: 119564 KB, 시간: 640 ms

### 분류

구현, 정렬

### 제출 일자

2023년 12월 24일 07:50:07

### 문제 설명

<p>Crianças adoram brincar com pequenos cubos. Elas passam horas criando ‘casas’, ‘prédios’, etc. O irmãozinho de Tomaz acabou de ganhar um conjunto de blocos coloridos no seu aniversário. Cada face de cada cubo é de uma cor.</p>

<p>Como Tomaz é uma criança muito analítica, ele decidiu descobrir quantos “tipos” diferentes de cubos o seu irmãozinho ganhou. Você pode ajuda-lo? Dois cubos são considerados do mesmo tipo se for possível rotacionar um deles de forma que as cores nas faces respectivas dos dois blocos sejam iguais.</p>

### 입력 

 <p>A entrada contém vários casos de teste. A primeira linha do caso de teste contém um inteiro N especificando o número de cubos no conjunto (1 ≤ N ≤ 1000). As próximas 3 x N linhas descrevem os cubos do conjunto. Na descrição as cores serão identificadas pelos números de 0 a 9. A descrição de cada cubo será dada em três linhas mostrando as cores das seis faces do cubo “aberto”, no formato dado no exemplo abaixo. No exemplo abaixo, as faces do cubo tem cores de 1 a 6, a face com cor 1 está no lado oposto da face com a cor 3, e a face com cor 2 é vizinha das faces 1, 3, 4 e 6, e está no lado oposto da face com cor 5.</p>

<p>1<br>
2 4 5 6<br>
3</p>

<p>O final da entrada é indicado por N = 0.</p>

### 출력 

 <p>Para cada caso de teste seu programa deve imprimir uma linha contendo um único inteiro, correspondente ao numero de tipos de cubos no conjunto dado.</p>

