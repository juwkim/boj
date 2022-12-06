# [Silver V] Jackpot - 6709 

[문제 링크](https://www.acmicpc.net/problem/6709) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

유클리드 호제법(euclidean), 수학(math), 정수론(number_theory)

### 문제 설명

<p>Bill has found the perfect way to make money playing the slot machines. After months of careful research, he has finally figured out the mechanics behind how the machines operate. Now he is ready to make profit of his findings.</p>

<p>But first an introduction to the game. A slot machine consists of a number of wheels, usually three or four, each with a number of symbols printed on it – cherries, oranges, bells, etc. – and will show one of its symbols at a given time. To play, you insert a coin, push a button and the wheels start spinning. After spinning for a while, each wheel stops – at random it seems – at one of its symbols. If all wheels stop at the same symbol, or some nice combination of symbols, the player wins. One combination that is especially desirable is having the jackpot symbol on all wheels. This combination is simply called ’jackpot’ and will make you rich for life.</p>

<p>What Bill has discovered is that each wheel will stop at the jackpot symbol with a certain periodicity, which differs a lot between wheels. He has also figured out (after some sneeking around at the slot-machine factory) that all newly manufactured slot-machines are delivered showing the jackpot combination, and that they all have a counter at the back, telling how many times the machine has been played. This counter is always set to zero at delivery.</p>

<p>Now, all Bill needs to do is to calculate the number of times a machine has to be played between two occurrences of the jackpot combination. We will call this number the jackpot periodicity. This is of course the same as the number of times the machine has to be played after leaving the factory, before it gives its first jackpot. Thus, with a glance at the counter on the back of a machine, Bill can figure out if it is about to give a jackpot.</p>

<p>As Bill knows that you are a skillful computer programmer, he turns to you with the problem of calculating the jackpot periodicity. For each machine, he will give you the number of wheels, and the periodicity with which the jackpot symbol shows up on each wheel.</p>

### 입력 

 <p>One line with the number of machines n ≤ 20. For each machine, one line with the number of wheels w ≤ 5, and one line with w numbers, p<sub>1</sub>, ..., p<sub>w</sub> the periodicity of each wheel p<sub>k</sub> ≤ 1000.</p>

### 출력 

 <p>One line per machine: The jackpot periodicity of the machine, if it is less than or equal to a billion (10<sup>9</sup>), otherwise output the text ’More than a billion.’.</p>

