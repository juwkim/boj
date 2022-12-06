# [Silver V] The Friend of My Enemy is My Enemy - 9255 

[문제 링크](https://www.acmicpc.net/problem/9255) 

### 성능 요약

메모리: 115004 KB, 시간: 144 ms

### 분류

그래프 이론(graphs), 구현(implementation)

### 문제 설명

<p>The NSA and various other agencies have a keen interest in tracking meta-data of phone calls and other interactions (e-mails) in order to build a network of who seems to be friends with whom. In fact, the government claims that the content of phone calls has not been spied upon, and only the meta-data (who called whom when and for how long) is being logged. The idea is that calling patterns will reveal social connections.</p>

<p>Part of the idea of building this network is that years later, when one person turns out to have been a terrorist, the agency can go through all their contacts to obtain leads to other potential terrorists. Of course, in many cases, “guilt by association” is an incredibly slippery slope in terms of ethical concerns, and any civilized society needs to be very careful when it considers someone potentially guilty. Notwithstanding such concerns, social network analysis algorithms seem to be a technique in intelligence that is here to stay, so we better understand them.</p>

<p>In this question, you will be given a network of who is friends (or associated) with whom, and the identity of one enemy. Your task is to output all friends of that person in the network, presumably for further investigation.</p>

### 입력 

 <p>The first line is the number K of input data sets, followed by the K data sets, each of the following form:</p>

<p>The first line contains two integers n, m, separated by a space. 1 ≤ n ≤ 100 is the number of people in your network. 0 ≤ m ≤ 10000 is the number of friendships among pairs of people.</p>

<p>Next come m lines, each containing two distinct integers between 1 and n, describing a connection between those two people.</p>

<p>Finally, on one more line, is a number s, 1 ≤ s ≤ n, the identity of the suspicious person we start from.</p>

### 출력 

 <p>For each data set, output “Data Set x:” on a line by itself, where x is its number. Then, output on one line all the direct friends of person s in the network, sorted in increasing order, separated by a space. (No person is friends with himself/herself, and we are not interested in friends-of-friends etc.) Each data set should be followed by a blank line.</p>

