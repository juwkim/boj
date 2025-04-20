# [Silver I] Fatorial - 13600 

[문제 링크](https://www.acmicpc.net/problem/13600) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

다이나믹 프로그래밍, 그리디 알고리즘, 수학

### 제출 일자

2025년 4월 20일 19:12:42

### 문제 설명

<p>O fatorial de um número inteiro positivo N, denotado por N!, é definido como o produto dos inteiros positivos menores do que ou iguais a N. Por exemplo 4! = 4 × 3 × 2 × 1 = 24.</p>

<p>Dado um inteiro positivo N, você deve escrever um programa para determinar o menor número k tal que N = a<sub>1</sub>! + a<sub>2</sub>! + ... + a<sub>k</sub>!, onde cada a<sub>i</sub>, para 1 ≤ i ≤ k, é um número inteiro positivo.</p>

<p>Por exemplo, para N = 10 a resposta é 3, pois é possível escrever N como a soma de três números fatoriais: 10 = 3! + 2! + 2!. Para N = 25 a resposta é 2, pois é possível escrever N como a soma de dois números fatoriais: 25 = 4! + 1!.</p>

### 입력 

 <p>A entrada consiste de uma única linha que contém um inteiro N (1 ≤ N ≤ 10<sup>5</sup>).</p>

### 출력 

 <p>Seu programa deve produzir uma única linha com um inteiro representando a menor quantidade de números fatoriais cuja soma é igual ao valor de N.</p>

