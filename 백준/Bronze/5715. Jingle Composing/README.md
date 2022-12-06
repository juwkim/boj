# [Bronze II] Jingle Composing - 5715 

[문제 링크](https://www.acmicpc.net/problem/5715) 

### 성능 요약

메모리: 28776 KB, 시간: 2448 ms

### 분류

사칙연산(arithmetic), 수학(math), 문자열(string)

### 문제 설명

<p>A. C. Marcos is taking his first steps in the direction of jingle composition. He is having some troubles, but at least he is achieving pleasant melodies and attractive rhythms.</p>

<p>In music, a note has a pitch (its frequency, resulting in how high or low is the sound) and a duration (for how long the note should sound). In this problem we are interested only in the duration of the notes.</p>

<p>A jingle is divided into a sequence of measures, and a measure is formed by a series of notes. </p>

<p>The duration of a note is indicated by its shape. In this problem, we will use uppercase letters to indicate a note’s duration. The following table lists all the available notes:</p>

<p style="text-align: center;"><img alt="" src="" style="height:86px; width:389px"></p>

<p>The duration of a measure is the sum of the durations of its notes. In Marcos’ jingles, each measure has the same duration. As Marcos is just a beginner, his famous teacher Johann Sebastian III taught him that the duration of a measure must always be 1.</p>

<p>For example, Marcos wrote a composition containing five measures, of which the first four have the correct duration and the last one is wrong. In the example below, each measure is surrounded with slashes and each note is represented as in the table above.</p>

<p style="text-align: center;">/HH/QQQQ/XXXTXTEQH/W/HW/</p>

<p>Marcos likes computers as much as music. He wants you to write a program that determines, for each one of his compositions, how many measures have the right duration.</p>

### 입력 

 <p>The input contains several test cases. Each test case is described in a single line containing a string whose length is between 3 and 200 characters, inclusive, representing a composition. A composition begins and ends with a slash ‘/’. Measures in a composition are separated by a slash ‘/’. Each note in a measure is represented by the corresponding uppercase letter, as described above. You may assume that each composition contains at least one measure and that each measure contains at least one note. All characters in the input will be either slashes or one of the seven uppercase letters used to represent notes, as described above.</p>

<p>The last test case is followed by a line containing a single asterisk.</p>

### 출력 

 <p>For each test case your program must output a single line, containing a single integer, the number of measures that have the right duration.</p>

