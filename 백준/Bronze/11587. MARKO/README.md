# [Bronze II] MARKO - 11587 

[문제 링크](https://www.acmicpc.net/problem/11587) 

### 성능 요약

메모리: 29452 KB, 시간: 220 ms

### 분류

Empty

### 문제 설명

<p>Good old Marko came across a new feature on his mobile phone – T9 input! His phone has a keyboard consisting of numbers looking like this:</p>

<p style="text-align:center"><img alt="" src="" style="height:128px; width:145px"></p>

<p>In order to input a word using this keyboard, one needs to press a key multiple times for the required letter. More specifically, if the required letter is the first letter mapped to the key, one key press is needed, if it’s the second, two key presses are needed and so on. For instance, if we want to input the word “giht”, we will press the following keys: g-4 i-444 h-44 t-8. The new possibility Marko discovered enables you to input text more easily because you don’t need several presses per letter anymore, just one. The software will try to figure out what word from the dictionary you are trying to input.</p>

<p>Marko is quite sceptical of new technologies (at least new for him) and he is afraid that errors will be frequent. That is the reason why he decided to test his hypothesis that the errors are frequent. Marko knows by heart the whole dictionary in the mobile phone. The dictionary consists of N words consisting of lowercase letters from the English alphabet, the total length of the word not exceeding 1 000 000 characters. He will give an array of key presses S, of total length at most 1 000, and wants to know how many words from the dictionary can be mapped to the given array of key presses if the T9 input feature is used.</p>

### 입력 

 <p>The first line of input contains the integer N, the number of words in the dictionary. (1 ≤ N ≤ 1 000). Each of the following N lines contains a single word. The last line of input contains the string S (1 ≤ |S| ≤ 1000) consisting of digits 2-9.</p>

### 출력 

 <p>The first and only line of output must contain the number of words from the dictionary possible to construct from the letters on the keys determined by the string S.</p>

