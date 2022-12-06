# [Bronze I] Hoof, Paper, Scissors (Bronze) - 14456 

[문제 링크](https://www.acmicpc.net/problem/14456) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>You have probably heard of the game "Rock, Paper, Scissors". The cows like to play a similar game they call "Hoof, Paper, Scissors".</p>

<p>The rules of "Hoof, Paper, Scissors" are simple. Two cows play against each-other. They both count to three and then each simultaneously makes a gesture that represents either a hoof, a piece of paper, or a pair of scissors. Hoof beats scissors (since a hoof can smash a pair of scissors), scissors beats paper (since scissors can cut paper), and paper beats hoof (since the hoof can get a papercut). For example, if the first cow makes a "hoof" gesture and the second a "paper" gesture, then the second cow wins. Of course, it is also possible to tie, if both cows make the same gesture.</p>

<p>Farmer John watches in fascination as two of his cows play a series of N games of "Hoof, Paper, Scissors" (1 ≤ N ≤ 100). Unfortunately, while he can see that the cows are making three distinct types of gestures, he can't tell which one represents "hoof", which one represents "paper" and which one represents "scissors" (to Farmer John's untrained eye, they all seem to be variations on "hoof"...)</p>

<p>Not knowing the meaning of the three gestures, Farmer John assigns them numbers 1, 2, and 3. Perhaps gesture 1 stands for "hoof", or maybe it stands for "paper"; the meaning is not clear to him. Given the gestures made by both cows over all N games, please help Farmer John determine the maximum possible number of games the first cow could have possibly won, given an appropriate mapping between numbers and their respective gestures.</p>

### 입력 

 <p>The first line of the input file contains N.</p>

<p>Each of the remaining N lines contain two integers (each 1, 2, or 3), describing a game from Farmer John's perspective.</p>

### 출력 

 <p>Print the maximum number of games the first of the two cows could possibly have won.</p>

