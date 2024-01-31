# [Silver III] Elevador - 13662 

[문제 링크](https://www.acmicpc.net/problem/13662) 

### 성능 요약

메모리: 110272 KB, 시간: 124 ms

### 분류

기하학

### 제출 일자

2024년 1월 31일 19:55:58

### 문제 설명

<p>A FCC (Fábrica de Cilindros de Carbono) fabrica vários tipos de cilindros de carbono. A FCC está instalada no décimo andar de um prédio, e utiliza os vários elevadores do prédio para transportar os cilindros. Por questão de segurança, os cilindros devem ser transportados na posição vertical; como são pesados, no máximo dois cilindros podem ser transportados em uma única viagem de elevador. Os elevadores têm formato de paralelepípedo e sempre têm altura maior que a altura dos cilindros.<br>
<br>
Para minimizar o número de viagens de elevador para transportar os cilindros, a FCC quer, sempre que possível, colocar dois cilindros no elevador. A figura abaixo ilustra, esquematicamente (vista superior), um caso em que isto é possível (a), e um caso em que isto não é possível (b):</p>

<p><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/13662/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202017-01-12%20%EC%98%A4%EC%A0%84%206.27.01.png" style="height:141px; width:328px"></p>

<p>Como existe uma quantidade muito grande de elevadores e de tipos de cilindros, a FCC quer que você escreva um programa que, dadas as dimensões do elevador e dos dois cilindros, determine se é possível colocar os dois cilindros no elevador.</p>

### 입력 

 <p>A entrada contém vários casos de teste. A primeira e única linha de cada caso de teste contém quatro números inteiros L, C, R<sub>1</sub> e R<sub>2</sub>, separados por espaços em branco, indicando respectivamente a largura do elevador (1 ≤ L ≤ 100), o comprimento do elevador (1 ≤ C ≤ 100), e os raios dos cilindros (1 ≤ R<sub>1</sub>, R<sub>2</sub> ≤ 100).</p>

<p>O último caso de teste é seguido por uma linha que contém quatro zeros separados por espaços em branco.</p>

### 출력 

 <p>Para cada caso de teste, o seu programa deve imprimir uma única linha com um único caractere: ‘S’ se for possível colocar os dois cilindros no elevador e ‘N’ caso contrário.</p>

