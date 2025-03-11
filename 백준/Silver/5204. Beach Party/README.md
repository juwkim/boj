# [Silver II] Beach Party - 5204 

[문제 링크](https://www.acmicpc.net/problem/5204) 

### 성능 요약

메모리: 111936 KB, 시간: 2352 ms

### 분류

브루트포스 알고리즘, 조합론, 수학

### 제출 일자

2025년 3월 11일 22:19:10

### 문제 설명

<p>For a rousing finale of a nice day at the beach, we are hanging around for a party, where various music groups set up stages, and perform, while people listen, dance, sing along out of tune, write their CS201 programming assignment, or do any number of other things. As there are many groups playing, everyone will simply flock to the music they like best. Unluckily, this sometimes means that you end up in a different place from most of your friends.</p>

<p>For instance, suppose that there are two stages, and on one of them, they perform Gregorian Chant, while the other one has Polkas.<sup>6</sup> You prefer Chant, but your best friend prefers Polkas. Now, if only instead of Polkas, they were playing Country (which your friend hates), he would come listen to Chant with you. So we may be wondering, given a choice of music styles, which ones, if assigned to stages, would result in the largest number of friends staying with you.</p>

<p>More formally, there are s stages, and m ≥ s music styles. Each stage has to get exactly one music style, and no style can be played on two stages. Each person, including you, has a preference order on styles, and will simply go to the stage with the most preferred music. The question is which assignment of music to stages will have the largest number of friends at the same stage as you.</p>

### 입력 

 <p>The first line contains a number K ≥ 1, which is the number of input data sets in the file. This is followed by K data sets of the following form:</p>

<p>The first line of the data set contains three numbers s, m, n, the number of stages, music styles, and friends (1 ≤ s ≤ 10, 1 ≤ m ≤ 20, 1 ≤ n ≤ 100). This is followed by n lines, each describing one friend (the first one being yourself). Each friend description is a permutation of the music styles {1, . . . , m}.</p>

### 출력 

 <p>For each data set, first output “Data Set x:” on a line by itself, where x is its number. Then, output the maximum number of friends (including yourself) that will listen to the same music as you for the most favorable assignment of music to stages. (Notice that you do not need to output the actual assignment achieving the maximum.)</p>

