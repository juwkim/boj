# [Silver I] Isósceles - 13588 

[문제 링크](https://www.acmicpc.net/problem/13588) 

### 성능 요약

메모리: 1312 KB, 시간: 972 ms

### 분류

구현

### 제출 일자

2025년 6월 30일 01:31:28

### 문제 설명

<p>Os irmãos Sérgio e Luiz estavam brincando com cubinhos de madeira e queriam construir um muro, que acabou ficando incompleto, com as colunas tendo diferentes alturas, como nessa figura.</p>

<p><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/13588/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202017-01-05%20%EC%98%A4%ED%9B%84%206.04.52.png" style="height:128px; width:350px"></p>

<p>Eles decidiram agora que a brincadeira seria retirar cubinhos, sempre de cima para baixo nas colunas, de maneira que no final restasse apenas um triângulo isósceles de cubinhos. Eles podem apenas retirar cubinhos do muro, sem recolocar em outra coluna, e os triângulos têm que ser completos. A figura abaixo ilustra os cinco primeiros triângulos isósceles de cubinhos, do tipo que eles querem, com alturas 1, 2, 3, 4 e 5 respectivamente.</p>

<p><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/13588/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202017-01-05%20%EC%98%A4%ED%9B%84%206.04.57.png" style="height:68px; width:340px"></p>

<p>Dada a sequência de alturas das colunas do muro, seu programa deve ajudar Sérgio e Luiz a descobrir qual é a altura máxima que o triângulo poderia ter ao final. No muro da primeira figura, com 30 colunas de cubinhos, o triângulo mais alto possível teria altura igual a sete.</p>

### 입력 

 <p>A primeira linha da entrada contém um inteiro N, representando o número de colunas do muro. A segunda linha contém N inteiros A<sub>i</sub>, indicando as alturas de cada coluna.</p>

<p>Restrições</p>

<ul>
	<li>1 ≤ N ≤ 50000</li>
	<li>1 ≤ A<sub>i</sub> ≤ N</li>
</ul>

### 출력 

 <p>Seu programa deve produzir uma única linha com um inteiro H, representando a altura máxima que um triângulo poderia ter ao final.</p>

