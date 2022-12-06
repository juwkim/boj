# [Silver IV] Alphabet Animals - 18018 

[문제 링크](https://www.acmicpc.net/problem/18018) 

### 성능 요약

메모리: 38788 KB, 시간: 136 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>You are playing a game in which a group of players take turns saying animal names. The animal name you say when it is your turn must start with the same letter as the previously said animal ends with and it must not have been said previously in this round of the game. If there is no valid name or you cannot come up with one you are eliminated.</p>

<p>Given the last animal name said before your turn and a list of all names not yet used, can you make it through this turn? If so, can you make sure to eliminate the next player?</p>

### 입력 

 <p>The first line of input contains a single word, the animal that the previous player just said. The next line contains a single integer n (0 ≤ n ≤ 10<sup>5</sup>), the number of valid unused animal names. Each of the following n lines contains one valid unused animal name.</p>

<p>All animal names (including the one the previous player said) are unique and consist of at least 1 and at most 20 lower case letters ‘a’-‘z’.</p>

### 출력 

 <p>If there is any animal name you can play that eliminates the next player, output the first such name from the input list, followed by an exclamation mark. Otherwise, if there is any animal name that you can play, output the first such name. Otherwise, output a question mark (in this case you will just have to make up a fake name in the hope that the others will trust you that this is a real animal).</p>

