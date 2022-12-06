# [Bronze I] Hex Code - 11784 

[문제 링크](https://www.acmicpc.net/problem/11784) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>In the movie The Martian (2015), astronaut Mark Watney, one of the crew members of Mission Ares III, was left behind on Mars due to an unexpected incident during the surface exploration on the planet Mars. The communication with Earth was quasi-inexistent. Fortunately, Mark Watney managed to establish a very simple way to communicate with NASA at the mission control base on Earth through hexadecimal codes.</p>

<p>Mark could receive one simple code at a time which he could detect as a hexadecimal digit or hex code including 0-9 and A-F. Then he could transform a pair of hex digits into a character since he knows how to look up the ASCII table. Fortunately enough he has an ASCII table at hand (who would miss an ASCII table on voyage to Mars!! ^_^). </p>

<p style="text-align: center;"><img alt="" src="" style="height:424px; width:500px"></p>

<p>If Mark receives a code sequence “4869204D61726B”, he can decode it into the message “Hi Mark”. However, decoding the hex codes manually is very slow and inefficient. Therefore your task is to help Mark Watney write a program to decode these hex codes. </p>

### 입력 

 <p>The input contains several lines of hex codes only (0-9, A-F). Each line contains an even number of hex digits that you have to transform into a plain text message. One pair of hex digits corresponds to a single character. There are less than 250 hex digits in each line. The input contains several lines of strings. You do not know in advance how many lines there are but it is guaranteed that the input contains less than 1,000 lines. </p>

### 출력 

 <p>For each line of hex codes, print out the corresponding text message. </p>

