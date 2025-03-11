# [Silver II] Shut The Box I - 5223 

[문제 링크](https://www.acmicpc.net/problem/5223) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

분류 없음

### 제출 일자

2025년 3월 11일 22:44:33

### 문제 설명

<p>Their pursuit of the Collector has taken the Avengers on a long voyage through the galaxies, and they are looking for ways to pass time on their ship. They discover an old game, called shut the box, that used to be popular with sailors. Each player starts with 9 cards, numbered 1 to 9, laid face-up (i.e., the number showing) on the table, and continues playing till he or she cannot make any moves.</p>

<p>The game is played with a pair of dice (with a small twist that, only one die is used if the total of the open cards is ≤ 6). Initially, all the cards are open (i.e., face-up). The player then roles the dice. Let the total dice value be m. The player selects any set of open cards whose face values sum to m, and closes (shuts) them by turning them face-down. For instance, say the player rolls a 6 and 2 the first time, with a total of 8. The player can shut either the card 8, or the cards 1 and 7, or the cards 2 and 6, or the three cards 1 and 2 and 5, and so on. As another example, if the current cards face up are: 1, 2, 6, and the player rolls a 4, then there are no cards that he can shut, and his turn is over.</p>

<p>The final score for the player is the sum of the numbers of the cards still face-up, and the aim is to get as low score as possible (and ideally to shut the box, i.e., have no cards left facing up). In the above case where the game ends with face up cards 1, 2, and 6, the final score is: 1 + 2 + 6 = 9.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/60a05c2d-7e0c-4e32-9d69-c24a4b6e68b4/-/preview/" style="width: 512px; height: 261px;"></p>

<p style="text-align: center;">Figure 1: Illustration of Shut the Box game in two cases (in the right example, only the last few moves are shown). Note that, we only use 1 die when the total of open cards is less than or equal to 6 (in the right example)</p>

<p>Dr. Banner (The Hulk) has heard of the following strategy. Consider all the valid alternatives for shutting cards, given the current roll of the dice. If there is only one, do it. If there are more than one, take the one that maximizes the smallest face value. (For example, given the options {1,7} and {2,6}, you would take {2,6}.) If there are many that maximize the smallest face value, take the one that maximizes the second smallest face value. (For example, given the options {2,4,6} and {2,3,7}, you would take {2,4,6}.) In general, among the valid options, select the one that maximizes the lexicographically ordered sequence of face values.</p>

<p>Your goal is to write a program to help Dr. Banner make this choice and, hopefully, win (you know the consequences of angering the Hulk).</p>

### 입력 

 <p>The first line in the test data file contains the number of test cases (< 100). After that, each line contains one test case: the first entry on each line is the rolled total (called target), and the next entry is the number of open cards n. The following n entries denote the open cards in the ascending order.</p>

### 출력 

 <p>For each test case, you are to output the best move according to the above strategy, or output that there is no legal move. The exact form is shown below.</p>

