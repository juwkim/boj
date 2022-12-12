# [Silver IV] Haja Ordenação - 23394 

[문제 링크](https://www.acmicpc.net/problem/23394) 

### 성능 요약

메모리: 47876 KB, 시간: 224 ms

### 분류

정렬(sorting)

### 문제 설명

<p>Um amigo seu inventou um jogo e quer saber se você consegue resolvê-lo ou se ele é impossível.</p>

<p>Ele montou uma sequencia de N blocos. Cada bloco tem um número gravado e uma cor. Todos os números são números distintos entre 1 e N, e blocos diferentes podem ter a mesma cor.</p>

<p>O jogo funciona da seguinte maneira: você pode jogar quantos turnos você quiser. Em um turno, você escolhe dois blocos diferentes que têm a mesma cor e os troca de posição.</p>

<p>Você deve dizer se é possível fazer com que a sequência inteira fique em ordem crescente ou não.</p>

### 입력 

 <p>A primeira linha contém dois inteiros N e K (1 ≤ N ≤ 10<sup>5</sup>, 1 ≤ K ≤ N), representando o número de blocos na sequência e o número de cores diferentes, respectivamente.</p>

<p>Cada uma das N linhas seguintes contém dois inteiros n<sub>i</sub> e c<sub>i</sub> (1 ≤ n<sub>i</sub> ≤ N, 1 ≤ c<sub>i</sub> ≤ K), representando o número e a cor do i-ésimo bloco, respectivamente.</p>

### 출력 

 <p>Imprima uma linha contendo um caracter. Se a sequência puder ser ordenada em ordem crescente, imprima a letra maiúscula ‘<code>Y</code>’; caso contrário, imprima a letra maiúscula ‘<code>N</code>’.</p>

