# [Silver II] Team Rankings - 4245 

[문제 링크](https://www.acmicpc.net/problem/4245) 

### 성능 요약

메모리: 110896 KB, 시간: 160 ms

### 분류

브루트포스 알고리즘, 구현

### 제출 일자

2025년 1월 13일 11:44:17

### 문제 설명

<p>It’s preseason and the local newspaper wants to publish a preseason ranking of the teams in the local amateur basketball league. The teams are the Ants, the Buckets, the Cats, the Dribblers, and the Elephants. When Scoop McGee, sports editor of the paper, gets the rankings from the selected local experts down at the hardware store, he’s dismayed to find that there doesn’t appear to be total agreement and so he’s wondering what ranking to publish that would most accurately reflect the rankings he got from the experts. He’s found that finding the median ranking from among all possible rankings is one way to go.</p>

<p>The median ranking is computed as follows: Given any two rankings, for instance ACDBE and ABCDE, the distance between the two rankings is defined as the total number of pairs of teams that are given different relative orderings. In our example, the pair B, C is given a different ordering by the two rankings. (The first ranking has C above B while the second ranking has the opposite.) The only other pair that the two rankings disagree on is B, D; thus, the distance between these two rankings is 2. The median ranking of a set of rankings is that ranking whose sum of distances to all the given rankings is minimal. (Note we could have more than one median ranking.) The median ranking may or may not be one of the given rankings.</p>

<p>Suppose there are 4 voters that have given the rankings: ABDCE, BACDE, ABCED and ACBDE. Consider two candidate median rankings ABCDE and CDEAB. The sum of distances from the ranking ABCDE to the four voted rankings is 1 + 1 + 1 + 1 = 4. We’ll call this sum the value of the ranking ABCDE. The value of the ranking CDEAB is 7 + 7 + 7 + 5 = 26.</p>

<p>It turns out that ABCDE is in fact the median ranking with a value of 4.</p>

### 입력 

 <p>There will be multiple input sets. Input for each set is a positive integer n on a line by itself, followed by n lines (n no more than 100), each containing a permutation of the letters A, B, C, D and E, left-justified with no spaces. The final input set is followed by a line containing a 0, indicating end of input.</p>

### 출력 

 <p>Output for each input set should be one line of the form:</p>

<pre>ranking is the median ranking with value value. </pre>

<p>Of course ranking should be replaced by the correct ranking and value with the correct value. If there is more than one median ranking, you should output the one which comes first alphabetically</p>

