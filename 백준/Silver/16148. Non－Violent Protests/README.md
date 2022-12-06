# [Silver V] Non-Violent Protests - 16148 

[문제 링크](https://www.acmicpc.net/problem/16148) 

### 성능 요약

메모리: 276612 KB, 시간: 908 ms

### 분류

정렬(sorting)

### 문제 설명

<p>Another historic event in 1968 was the assassination of Martin Luther King Jr. He was a leader of the Civil Rights Movement, and his “I have a dream” speech is considered one of the most important speeches in American history. Martin Luther King Jr. was an unwavering advocate for non-violent protests. The reason non-violent protests tend to be more effective is that the goal of protests is typically to raise awareness and sway public opinion. It is much harder to sway public opinion in your favor when you are perceived as violent. Not surprisingly, then, police and other organizations tried to undermine the Civil Rights movement by aggressive provocation, as well as by planting violent protesters in the hopes that they would lead entire protests to follow their example and start large-scale riots. One important point that this raises is that for a protest in a tense environment, the line between a peaceful protest and a riot is often very thin. While reports in the media (and in history books) will typically treat the character of the whole group as “uniform,” in reality, these are individuals reacting to a particular situation, and very subtle changes in the situation may lead to different outcomes.</p>

<p>We will explore this with a simplified model, as follows. n individuals are participating in a protest. Each individual has an integer threshold t<sub>i</sub> ≥ 0. Individual i will riot if at least t<sub>i</sub> other people are already rioting before him. In turn, he may thus cause others to riot, too. Starting from no one rioting, you are to compute how many people will riot at the end.</p>

### 입력 

 <p>The first line is the number K of input data sets, followed by K data sets, each of the following form:</p>

<p>The first line is the number 0 ≤ n ≤ 1000000 of individuals. This is followed by a line with the n thresholds t<sub>i</sub> of the individuals, given in no particular order.</p>

### 출력 

 <p>For each data set, output “Data Set x:” on a line by itself, where x is its number. Then, output the number of people who riot at the end.</p>

<p>Each data set should be followed by a blank line.</p>

