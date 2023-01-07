# [Silver IV] Aku Negaraku - 15832 

[문제 링크](https://www.acmicpc.net/problem/15832) 

### 성능 요약

메모리: 119168 KB, 시간: 592 ms

### 분류

자료 구조(data_structures), 큐(queue)

### 문제 설명

<p>1st Academy is an international leadership training academy based in Kuala Lumpur. Every year, the company trains thousands of people to be supplied to companies around the world. To be fair amongst all the trainees, the company will do the selection process using numbering system. The trainees will choose a number from 1 to N, and one number is not limited to only one trainee. The N represents the total number of companies that request trainees from the academy. A number, M, would be picked at random, and the selection starts with a trainee whose number is 1, and then in every M’th people after that, wrapping around to 1 after N, and ignoring trainees already selected. For example, if N = 15 and M = 6, trainees would be selected in the order: 6, 12, 3, 10, 2, 11, 5, 15, 13, 9, 14, 4, 1, 8, 7. All the selected trainees except the last one (which is number 7) will be supplied to companies outside of Malaysia.</p>

<p>However, Leong preferred to stay and work in Malaysia. To him, there is no better place other than Malaysia. He does not mind being located anywhere as long it is Malaysia. As a friend of him, you could help him to choose a number that will save him from being located outside.</p>

### 입력 

 <p>Input will consist of a series of lines, each line containing the number of companies (N) with 1 ≤ N ≤ 1500, and a skipping value (M) with 1 ≤ M ≤ 50. The values will be terminated by a line consisting of double zeros (0 0) as shown in sample input output.</p>

### 출력 

 <p>Output will consist of a series of lines, one for each line of the input. Each line will consist of the number M according to the above scheme.</p>

