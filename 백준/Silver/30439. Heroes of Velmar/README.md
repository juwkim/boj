# [Silver V] Heroes of Velmar - 30439 

[문제 링크](https://www.acmicpc.net/problem/30439) 

### 성능 요약

메모리: 108080 KB, 시간: 84 ms

### 분류

구현

### 제출 일자

2024년 10월 19일 15:00:26

### 문제 설명

<p>Welcome to the world of <em>Heroes of Velmar</em>, the critically acclaimed trading card game developed by <em>Sidney Games</em>! After the tremendous success of the physical card game, Sidney Games has decided to take it to the next level and transform it into an immersive video game experience.</p>

<p>As Sidney Games embarks on this ambitious video game project, they seek the expertise of talented developers like you to bring this digital version to life. The challenge lies in coding the algorithm that determines the winner in the virtual battles that unfold between players. The video game will need to retain the same core mechanics as the original card game, where players compete on three distinct locations over six turns, with abilities and power levels shaping the outcomes.</p>

<p>The full rules of the game are listed below. You are given the state of the locations after <em>Setup</em> and <em>Gameplay</em> have finished and the <em>End of the Game</em> has been reached. Sidney Games has tasked you with implementing the <em>Location Resolution</em> part of the game rules, including the application of <em>Special Abilities</em>, to determine the winner.</p>

<p>The game designers have provided you with images of the cards as well as a JSON file with their specifications.</p>

### 입력 

 <p>Input consists of six lines representing the state of the three locations after six turns of play. This means that there will be at most 24 cards total listed in the input.</p>

<p>First the left location is described, then the center location is described, and finally the right location is described. Each location is described by two lines, the first of which represents player 1's cards and the second of which represents player 2's cards. Each line lists the number of cards in the line and then the names of the cards played by the player, separated by spaces. There will be at most four cards in each line.</p>

<p>Note that a player may leave a location empty. Each input is guaranteed to be a valid reachable final game state according to the game rules.</p>

### 출력 

 <p>Output <code>"Player 1"</code> if player 1 won, <code>"Player 2"</code> if player 2 won, or <code>"Tie"</code> if there was no victor.</p>

