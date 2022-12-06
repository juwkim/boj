# [Bronze I] Coral Perfeito - 13638 

[문제 링크](https://www.acmicpc.net/problem/13638) 

### 성능 요약

메모리: 30840 KB, 시간: 80 ms

### 분류

그리디 알고리즘(greedy), 구현(implementation), 수학(math)

### 문제 설명

<p>A Maestrina do coral está planejando o espetáculo que apresentará na famosa Semana Brasileira de Corais. Ela pensou em preparar uma nova música, definida da seguinte maneira:</p>

<ul>
	<li>cada um dos integrantes do coral inicia cantando uma nota, e somente muda de nota quando determinado pela Maestrina;</li>
	<li>ao final de cada compasso, a Maestrina determina que exatamente dois integrantes alterem a nota que cantam: um integrante passa a cantar a nota imediatamente acima da nota que cantava, e o outro integrante passa a cantar a nota imediatamente abaixo da nota que cantava;</li>
	<li>a música termina ao final do primeiro compasso em que todos os integrantes do coral cantam a mesma nota.</li>
</ul>

<p>A Maestrina já tem várias ideias de como distribuir as notas no início da música entre os integrantes do coral, de forma a criar o efeito desejado. No entanto, ela está preocupada em saber se, dada uma distribuição de notas entre os integrantes, é possível chegar ao final da música da forma desejada (todos cantando a mesma nota) e, caso seja possível, qual o número mínimo de compassos da música. Você pode ajudá-la?</p>

### 입력 

 <p>A primeira linha de um caso de teste contém um inteiro N indicando o número de integrantes do coral. As notas serão indicadas por números inteiros. A segunda linha contém N números inteiros, indicando as notas iniciais que cada integrante deve cantar. As notas são dadas em ordem não decrescente de altura.</p>

<p>Restrições</p>

<ul>
	<li>2 ≤ N ≤ 10<sup>4</sup></li>
	<li>−10<sup>5</sup> ≤ notai ≤ 10<sup>5</sup> para 0 ≤ i ≤ N − 1</li>
	<li>nota<sub>i</sub> ≤ nota<sub>i+1</sub> para 0 ≤ i ≤ N − 2</li>
</ul>

### 출력 

 <p>Para cada caso de teste imprima uma linha contendo um único número inteiro indicando o número mínimo de compassos que a música terá. Se não é possível terminar a música com todos os integrantes cantando a mesma nota, imprima o valor −1.</p>

