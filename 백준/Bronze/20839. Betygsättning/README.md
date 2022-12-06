# [Bronze IV] Betygsättning - 20839 

[문제 링크](https://www.acmicpc.net/problem/20839) 

### 성능 요약

메모리: 29200 KB, 시간: 68 ms

### 분류

많은 조건 분기(case_work), 구현(implementation)

### 문제 설명

<p>Pelle är programmeringslärare på Pelles Optimeringsskola (PO-skolan). Han håller nu på att sätta betyg på sina elever i kursen Optimering $1$.</p>

<p>Betygsättning går till på följande vis. Totalt finns det $x$ <code>A</code>-kriterier, $y$ <code>C</code>-kriterier och $z$ <code>E</code>-kriterier som används. För att få betyget <code>E</code> måste man uppfylla samtliga <code>E</code>-kriterier. För att få betyget <code>C</code> måste man uppfylla samtliga <code>C</code>- och <code>E</code>-kriterier. För att få betyget <code>A</code> måste man uppfylla samtliga <code>A</code>-, <code>C</code>- och <code>E</code>-kriterier.</p>

<p>Dessutom finns det två speciella betyg. Om man uppfyller alla <code>E</code>-kriterier och minst hälften av <code>C</code>-kriterierna får man ett <code>D</code>. Om man uppfyller alla <code>E</code>- och <code>C</code>-kriterier och minst hälften av <code>A</code>-kriterierna får man ett <code>B</code>.</p>

<p>Pelle tycker det är väldigt jobbigt att sätta betyg, och behöver din hjälp. Skriv ett program som tar emot antalet <code>A</code>-, <code>C</code>- och <code>E</code>-kriterier en viss elev har uppfyllt och skriver ut vilket betyg eleven ska ha. Du kan anta att eleven alltid fick minst <code>E</code> i kursen.</p>

### 입력 

 <p>På första raden står tre heltal $1 \leq x \leq 30$, $1 \leq y \leq 30$ och $1 \leq z \leq 30$, antalet <code>A</code>-, <code>C</code>- och <code>E</code>-kriterier som finns. På den andra raden står tre heltal $0 \leq x' \leq x$, $0 \leq y' \leq y$ och $0 \leq z' \leq z$, antalet <code>A</code>-, <code>C</code>- och <code>E</code>-kriterier som eleven har uppfyllt.</p>

### 출력 

 <p>Programmet ska skriva ut en bokstav: <code>A</code>, <code>B</code>, <code>C</code>, <code>D</code>, eller <code>E</code>.</p>

