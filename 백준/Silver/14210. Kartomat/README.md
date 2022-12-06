# [Silver V] Kartomat - 14210 

[문제 링크](https://www.acmicpc.net/problem/14210) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

Empty

### 문제 설명

<p>A ticket machine is a device similar to an ATM and was introduced by Croatian Railways in order to make purchasing train tickets easier. The first step in buying a ticket is choosing the destination​ of your journey. The destination can be one of N destinations offered in advance, names of local and worldwide places. You choose your destination by typing its name letter by letter. By entering each additional letter, the number of possible destinations reduces.</p>

<p>The initial appearance of the keyboard on the screen is shown in the picture. We will represent it as four arrays of characters of length 8. </p>

<p><img alt="" src="" style="height:120px; width:482px"></p>

<p>After choosing each letter, the keyboard changes its appearance. Only letters that can be chosen in the next step are left active (depending on the destinations still possible to choose). The remaining letter that can’t be chosen are replaced with the character “*”.</p>

<p>Write a programme that will, for N given destinations and the first few letters (not all of them) of the chosen destination, output the appearance of the keyboard before entering the next letter. You will never be given the entire word. </p>

### 입력 

 <p>The first line contains the integer N (1 ≤ N ≤ 50) from the task. Each of the following N lines contains one string of at most 100 characters that contains only uppercase letters of the English alphabet. The last line contains the string that represents the first few letters of the chosen destination. </p>

### 출력 

 <p>You must output the appearance of the keyboard described in the task. </p>

