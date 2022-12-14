# [Bronze I] Командная олимпиада - 22103 

[문제 링크](https://www.acmicpc.net/problem/22103) 

### 성능 요약

메모리: 30840 KB, 시간: 176 ms

### 분류

사칙연산(arithmetic), 브루트포스 알고리즘(bruteforcing), 수학(math)

### 문제 설명

<p>Вася с друзьями решил поучаствовать в новой командной олимпиаде. В отличие от привычных ему олимпиад, на этой олимпиаде в одной команде может быть любое число участников. Для победы команде необходимо решить все представленные задачи.</p>

<p>На олимпиаде предлагаются задачи двух типов: <i>n</i> интерактивных и <i>m</i> обычных задач. Каждый из друзей Васи умеет решать только задачи одного типа. Если друг умеет решать интерактивные задачи, то у него на каждую задачу уходит <i>p</i> минут, а если обычные — то <i>q</i> минут. Вася же умеет решать и те, и другие задачи, как и его друзья, он тратит <i>p</i> минут на интерактивную задачу и <i>q</i> минут на обычную.</p>

<p>Участники команды могут использовать для решения задач произвольное число компьютеров. При этом во время олимпиады каждую задачу решает ровно один участник, между собой участники не общаются.</p>

<p>Помогите Васе составить команду, которая сможет победить в олимпиаде продолжительностью <i>t</i> минут таким образом, чтобы в ней было как можно меньше человек.</p>

<p>Например, если на олимпиаде продолжительностью 100 минут предлагается 10 интерактивных и 10 обычных задач, <i>p</i> = <i>q</i> = 30, то можно составить команду из 7 человек: Васи, трех друзей, которые решают интерактивные задачи, и трех друзей, которые решают обычные задачи. Каждый из друзей решит по три задачи своего типа, а Вася решит одну интерактивную и одну обычную задачу.</p>

### 입력 

 <p>В первой строке задано число тестовых наборов <i>T</i> (1 ≤ <i>T</i> ≤ 1000). В следующих <i>T</i> строках заданы тестовые наборы: по пять целых положительных чисел <i>n</i>, <i>m</i>, <i>p</i>, <i>q</i>, <i>t</i>, каждое из которых не превышает 10000. Также, <i>p</i> ≤ <i>t</i> и <i>q</i> ≤ <i>t</i>.</p>

### 출력 

 <p>Для каждого тестового набора выведите единственное число на строке — минимальное число участников команды, необходимое, чтобы победить.</p>

