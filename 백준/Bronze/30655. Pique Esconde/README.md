# [Bronze III] Pique Esconde - 30655 

[문제 링크](https://www.acmicpc.net/problem/30655) 

### 성능 요약

메모리: 110404 KB, 시간: 136 ms

### 분류

브루트포스 알고리즘, 구현

### 제출 일자

2023년 11월 11일 10:31:05

### 문제 설명

<p>João, que gosta de informática, procura pensar em como seria um programa para automatizar tudo que ele faz no seu dia a dia. Maria o desafiou a fazer um programa que fosse útil de algum jeito para quando eles brincarem de pique esconde.</p>

<p>João teve uma ideia muito boa de um programa, mas como ele ainda está em suas primeiras aulas de informática, ainda não descobriu como implementar essa ideia. Assim, você deve ajudá-lo. A ideia de João é numerar as crianças participando da brincadeira de 1 a n. O programa recebe como entrada o número total de crianças e também o número correspondente 'a criança que está procurando os demais participantes. Depois, o programa recebe uma lista com n − 2 números identificando as crianças que já foram encontradas e deve responder qual a criança que está faltando.</p>

<p>Sua tarefa é implementar esse programa e ajudar João a mostrar para Maria que a informática pode ser útil até nas mais simples tarefas.</p>

### 입력 

 <p>A entrada é composta por diferentes casos de teste. A primeira linha de cada caso de teste contém n, o número de crianças, e m, o número da criança que está procurando as demais, 2 ≤ n ≤ 1000 e 1 ≤ m ≤ n. As n − 2 linhas seguintes contém um inteiro cada representando as crianças que já foram encontradas.</p>

<p>A entrada termina com n = m = 0. Essa linha não deve ser processada.</p>

### 출력 

 <p>Para cada caso de teste, seu programa deve imprimir uma linha contendo o número da criança que ainda não foi encontrada.</p>

