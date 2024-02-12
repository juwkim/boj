# [Silver III] Rank Order - 10442 

[문제 링크](https://www.acmicpc.net/problem/10442) 

### 성능 요약

메모리: 447872 KB, 시간: 3480 ms

### 분류

정렬

### 제출 일자

2024년 2월 12일 16:26:12

### 문제 설명

<p>Your team has been retained by the director of a competition who supervises a panel of judges. The competition asks the judges to assign integer scores to competitors – the higher the score, the better. Although the event has standards for what score values mean, each judge is likely to interpret those standards differently. A score of 100, say, may mean different things to different judges.</p>

<p>The director's main objective is to determine which competitors should receive prizes for the top positions. Although absolute scores may differ from judge to judge, the director realizes that relative rankings provide the needed information – if two judges rank the same competitors first, second, third, ... then they agree on who should receive the prizes.</p>

<p>Your team is to write a program to assist the director by comparing the scores of pairs of judges. The program is to read two lists of integer scores in competitor order and determine the highest ranking place (first place being highest) at which the judges disagree.</p>

### 입력 

 <p>Input to your program will be a series of score list pairs. Each pair begins with a single integer giving the number of competitors N, 1 < N < 1,000,000. The next N integers are the scores from the first judge in competitor order. These are followed by the second judge's scores – N more integers, also in competitor order. Scores are in the range 0 to 100,000,000 inclusive. Judges are not allowed to give ties, so each judge’s scores will be unique. Values are separated from each other by one or more spaces and/or newlines. The last score list pair is followed by the end-of-file indicator.</p>

### 출력 

 <p>For each score pair, print a line with the integer representing the highest-ranking place at which the judges do not agree. If the judges agree on every place, print a line containing only the word 'agree'. Use the format below: “Case”, one space, the case number, a colon and one space, and the answer for that case with no trailing spaces.</p>

