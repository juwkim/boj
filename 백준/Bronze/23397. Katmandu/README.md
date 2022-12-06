# [Bronze III] Katmandu - 23397 

[문제 링크](https://www.acmicpc.net/problem/23397) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구현(implementation)

### 문제 설명

<p>Finalmente a pandemia está melhorando e você finalmente pode fazer a coisa com a qual esteve sonhando nos últimos anos: comer no seu restaurante favorito. Acontece que esse restaurante fica em Katmandu, mas tudo bem, é só você ir de avião.</p>

<p>O problema é que viajar de avião quase sempre te deixa muito cansado. Você se considera descansado se você consegue dormir por T minutos sem interrupção, ou seja, você nunca está acordado de um certo momento t até t + T. Além disso você dorme com muita facilidade: você consegue dormir no começo de qualquer minuto e acordar ao fim de qualquer minuto.</p>

<p>Claro que se você dormir demais você vai acabar perdendo todas as refeições que servem no vôo! Isso é completamente inaceitável: nenhuma oportunidade de comer de graça pode passar em branco.</p>

<p>Felizmente, a companhia aérea te mandou o cronograma completo do vôo: a duração do vôo, D minutos, o número de refeições que serão servidas, M, e o tempo a partir do início do vôo em que essas refeições serão servidas, y<sub>i</sub>. Você precisa estar acordado no início do minuto em que a refeição será servida para comê-la, caso contrário você não será servido. Como você está sempre com fome, a refeição será devorada instantaneamente.</p>

<p>Agora você quer saber, para ter o vôo perfeito, você consegue ficar descansado e ainda assim comer todas as refeições durante o vôo?</p>

### 입력 

 <p>A primeira linha da entrada contém três inteiros, T, D, M (1 ≤ T, D ≤ 10<sup>5</sup>, 0 ≤ M ≤ 1000), que representam, respectivamente, o número de minutos consecutivos que você precisa dormir para ficar descansado, a duração do vôo e o número de refeições que serão servidas durante o vôo.</p>

<p>Cada uma das M linhas seguintes contém um inteiro y<sub>i</sub> (0 ≤ y<sub>i</sub> ≤ D). Esses inteiros representam os tempos nos quais cada refeição será servida, e são dados em ordem cronológica.</p>

### 출력 

 <p>Imprima uma única linha contendo um único caractere. Se você consegue descansar durante o vôo e ainda assim comer todas as refeições, imprima ‘<code>Y</code>’; caso contrário, imprima ‘<code>N</code>’.</p>

