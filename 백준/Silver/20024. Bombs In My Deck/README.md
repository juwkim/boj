# [Silver V] Bombs In My Deck - 20024 

[문제 링크](https://www.acmicpc.net/problem/20024) 

### 성능 요약

메모리: 113248 KB, 시간: 108 ms

### 분류

수학(math), 확률론(probability)

### 문제 설명

<p>Donghyun is playing a digital card game. In this game, two players start with a deck (stack of cards) of $30$ cards and $30$ HP (health points). <br>
They alternate turns drawing and playing their cards. The winner is the first person who makes their opponent's HP less than or equal to $0$.</p>

<p>This time, Donghyun met a tough opponent; the opponent mixed some <strong>bombs</strong> into Donghyun's deck! Now, there are $A$ cards in Donghyun's deck, and $B$ of them are <strong>bombs</strong>. Each card in the deck is equally likely to be a bomb.</p>

<p>Donghyun starts his next turn with $C$ HP. On his next turn, he will remove cards from the top of his deck one at a time until he removes a card that is not a bomb or until his HP becomes less than or equal to 0. For each bomb that he removes, he loses 5 HP. Donghyun's deck is guaranteed to contain at least one card which is not a bomb, so this process is guaranteed to terminate.</p>

<p>Donghyun is worried he may lose the game because of the bombs. Specifically, he will lose the game if and only if his HP becomes less than or equal to $0$. Donghyun asks you to calculate the probability that he does not lose the game in his next turn.</p>

### 입력 

 <p>On the first and only line, three space-separated integers $A$, $B$, and $C$ are given. ($1 \le B < A \le 30$, $1 \le C \le 30$)</p>

<p>Donghyun has $A$ cards in his deck, $B$ of them are bombs, and his current HP is $C$.</p>

### 출력 

 <p>Output the probability that Donghyun survives after his next turn.</p>

<p>Your output will be considered correct if the absolute error between your answer and the jury's answer does not exceed $10^{-6}$.</p>

