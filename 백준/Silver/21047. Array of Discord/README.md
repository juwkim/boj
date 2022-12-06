# [Silver IV] Array of Discord - 21047 

[문제 링크](https://www.acmicpc.net/problem/21047) 

### 성능 요약

메모리: 113248 KB, 시간: 108 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구성적(constructive)

### 문제 설명

<p>Once upon a time, high up on Mount Olympus, it came to pass that the gods held a competition to see who among them was the best at sorting lists of integers.  Eris, the goddess of discord, finds this terribly boring and plans to add some mischief to the mix to make things more fun.  She will sabotage the answers of Zeus so that his list of numbers is no longer sorted, which will no doubt be so embarrassing that he becomes furious and starts a minor war.</p>

<p>Eris must be careful not to be discovered while performing her sabotage, so she decides to only change a single digit in one of the numbers in Zeus' answer.  The resulting number may not have any leading zeros (unless it becomes equal to zero in which case a single zero digit is allowed).  Eris can only replace a digit with another digit -- adding or removing digits is not allowed.</p>

### 입력 

 <p>The first line of input contains $n$ ($2 \leq n \leq 100$), the length of Zeus' answer.  The second line contains $n$ integers $a_1, a_2, \ldots, a_n$ ($0 \leq a_1 \le a_2 \le \ldots \le a_n \leq 10^{15}$), Zeus' answer.</p>

### 출력 

 <p>If Eris can make the list not be sorted by changing a single digit of one of the numbers, then output $n$ integers $b_1, \ldots, b_n$, the resulting list of numbers after making the change.  Otherwise, output "<code>impossible</code>".  If there are many valid solutions, any one will be accepted.</p>

