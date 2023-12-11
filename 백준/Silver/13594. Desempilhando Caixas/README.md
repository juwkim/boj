# [Silver IV] Desempilhando Caixas - 13594 

[문제 링크](https://www.acmicpc.net/problem/13594) 

### 성능 요약

메모리: 110404 KB, 시간: 124 ms

### 분류

애드 혹, 구현

### 제출 일자

2023년 12월 11일 23:19:46

### 문제 설명

<p>Joãozinho e sua família acabaram de se mudar. Antes da mudança, ele colocou todos os seus livros dentro de várias caixas numeradas. Para facilitar a retirada dos livros, ele fez um inventário, indicando em qual caixa cada livro foi colocado, e o guardou na caixa de número 1.</p>

<p>Chegando no seu novo quarto, ele viu que seus pais guardaram as caixas em várias pilhas, arrumadas em fila, com cada pilha encostada na pilha seguinte.</p>

<p>Joãozinho é um garoto muito sistemático. Por isso, antes de abrir qualquer outra caixa, ele quer recuperar seu inventário. Joãozinho também é um garoto muito desajeitado. Para tirar uma caixa de uma pilha, ele precisa que a caixa esteja no topo da pilha e que ao menos um de seus lados, não importa qual, esteja livre (isto é, não tenham nenhuma caixa adjacente).</p>

<p>Para isso, Joãozinho precisa desempilhar algumas das caixas. Como o quarto dele é bem grande, ele sempre tem espaço para colocar as caixas retiradas em outro lugar, sem mexer nas pilhas que os pais dele montaram.</p>

<p>Para minimizar seu esforço, Joãozinho quer que você escreva um programa que, dadas as posições das caixas nas pilhas, determine quantas caixas Joãozinho precisa desempilhar para recuperar seu inventário.</p>

### 입력 

 <p>A entrada é composta de vários casos de teste. A primeira linha de cada caso de teste contém dois números inteiros N e P , indicando, respectivamente, o número de caixas e o número de pilhas (1 ≤ P ≤ N ≤ 1.000). As caixas são numeradas seqüencialmente de 1 a N.</p>

<p>Cada uma das P linhas seguintes descreve uma pilha. Cada linha contém um inteiro Q<sub>i</sub>, indicando quantas caixas há na pilha i, seguido de um espaço em branco, seguido de uma lista de Q<sub>i</sub> números, que são os identificadores das caixas. Os elementos da lista são separados por um espaço em branco.</p>

<p>Todas as pilhas contêm pelo menos uma caixa, e todas as caixas aparecem exatamente uma vez na entrada. As caixas em cada pilha são listadas em ordem, da base até o topo da pilha. Todas as caixas têm o mesmo formato.</p>

<p>O final da entrada é indicado por N = P = 0.</p>

### 출력 

 <p>Para cada caso de teste da entrada, seu programa deve imprimir uma única linha, contendo um único inteiro: o número mínimo de caixas, além da caixa 1, que Joãozinho precisa desempilhar para recuperar o seu inventário.</p>

