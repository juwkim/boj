# [Bronze III] Ampelmännchen - 11434 

[문제 링크](https://www.acmicpc.net/problem/11434) 

### 성능 요약

메모리: 115440 KB, 시간: 148 ms

### 분류

사칙연산(arithmetic), 그리디 알고리즘(greedy), 수학(math)

### 문제 설명

<p>When you unite two countries, they will typically have their own versions of most things, like road signs, foods, etc. If you basically have one of the countries “impose” its version on the other, this may feel to the other more like an annexation than a unification of two equals.<sup>3</sup> So you need to be sure to take little bits and pieces of both countries and build a whole that’s acceptable to everyone. For instance, East Germans really liked their own versions of pickles and ketchup. In some cases, both sides agree that one country’s version is preferable — for instance, everyone loves the East German “Ampelmännchen,” the traffic signal pedestrian walk sign. It gets harder when each side prefers their own version — in that case, you need compromises such as “We really care about our pickles, so let’s keep them, but we like your ketchup almost as much, so we’re fine with yours.” Here, you will figure out suitable compromises for combining two cultures.</p>

<p>You will be given a list of contentious items, and for each of them how much each of the two countries like each version. You are also given how many people live in each of the two united countries. Your goal is to find out a choice for items that maximizes the total “happiness” of all people. That is the sum of the happinesses of everyone with all the items you select. For each item (e.g., “pickles”), you can only choose one of the two versions.</p>

<p><sup>3</sup>Indeed, many East Germans felt that way about the way the unification was carried out, and hence in many cases took a long time to “identify” with the new country.</p>

### 입력 

 <p>The first line contains a number K ≥ 1, which is the number of input data sets in the file. This is followed by K data sets of the following form:</p>

<p>The first line of each data set contains three integers n, W, E. 0 ≤ n ≤ 1000 is the number of contentious items. 0 ≤ W, E ≤ 10000 are the number of people living in the West and East.</p>

<p>This is followed by n lines, each containing four integers 0 ≤ L<sub>w,w</sub>, L<sub>w,e</sub>, L<sub>e,w</sub>, L<sub>e,e</sub> ≤ 100. These are, in order: how much the West likes its own version, how much the West likes the East’s version, how much the East likes the West’s version, and how much the East likes its own version.</p>

### 출력 

 <p>For each data set, first output “Data Set x:” on a line by itself, where x is its number. Then, output the maximum total happiness that can be produced by choosing exactly one version of each product.</p>

<p>Each data set should be followed by a blank line.</p>

