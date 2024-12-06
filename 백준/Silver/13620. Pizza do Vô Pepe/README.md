# [Silver IV] Pizza do Vô Pepe - 13620 

[문제 링크](https://www.acmicpc.net/problem/13620) 

### 성능 요약

메모리: 109544 KB, 시간: 88 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2024년 12월 6일 20:34:06

### 문제 설명

<p>Vovô Pepe é famoso por suas pizzas. Elas são deliciosas, e têm o formato de um círculo perfeito. Vovô preparou uma pizza especial para o jantar de hoje à noite, e colocou um certo número de azeitonas distribuídas aleatoriamente, mas colocadas exatamente na borda da pizza.</p>

<p>Sua tarefa é determinar, conhecendo a circunferência da pizza, a quantidade de azeitonas e a posição de cada azeitona, se é possível dividir a pizza em setores circulares de mesmo tamanho, de tal forma que cada pedaço de pizza contenha exatamente uma azeitona.</p>

<p>A figura abaixo mostra (a) uma pizza de circunferência 12 com 3 azeitonas e uma possível divisão em pedaços iguais; e (b) uma pizza de circunferência 12 com 4 azeitonas que não pode ser dividida em pedaços iguais como descrito acima. Apesar de deliciosas, as azeitonas são muito pequenas, e suas dimensões podem ser desconsideradas no cálculo da divisão.</p>

<p><img alt="" src="https://onlinejudgeimages.s3.amazonaws.com/problem/13620/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202017-01-05%20%EC%98%A4%ED%9B%84%207.06.39.png" style="height:187px; width:359px"></p>

### 입력 

 <p>A primeira linha contém dois inteiros C (3 ≤ C ≤ 10<sup>5</sup> ) e N (3 ≤ N ≤ 10<sup>4</sup> , N ≤ C) representando respectivamente a circunferência da pizza e o número de azeitonas. O inteiro C é múltiplo de N. A segunda linha contém N inteiros distintos X<sub>i</sub> (0 ≤ X<sub>1</sub> < X<sub>2</sub> < . . . < X<sub>N</sub> < C), em ordem crescente, descrevendo as posições das azeitonas, dadas pelo comprimento do arco circular no sentido horário, a partir de um ponto fixo da circunferência.</p>

### 출력 

 <p>Seu programa deve produzir apenas uma linha, com apenas uma letra, que deve ser S se é possível dividir a pizza como descrito acima, ou N caso contrário.</p>

