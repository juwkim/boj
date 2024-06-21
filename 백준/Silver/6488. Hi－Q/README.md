# [Silver III] Hi-Q - 6488 

[문제 링크](https://www.acmicpc.net/problem/6488) 

### 성능 요약

메모리: 109240 KB, 시간: 132 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2024년 6월 21일 21:42:22

### 문제 설명

<p>Hi-Q is a popular solitaire game that comes in a small box with a playing board that has little holes in the shape of a cross and 32 little pegs that fit into the holes. Starting with the centermost hole open, players move the pegs by jumping one peg over another, either in a horizontal or vertical direction and removing each peg that is jumped over. Diagonal jumps are not allowed. The object for players is to remove as many pegs from the board as possible. This problem involves writing a program that will automatically play Hi-Q so that we can investigate how the game might unfold based on various opening arrangements of pegs.</p>

<p>Problem Statement: There is a peg board with the following shape and with holes numbered from 1 to 33 as follows:</p>

<pre>                              1           2         3
                              4          5         6
       7          8         9         10        11          12        13
     14         15        16         17        18         19        20
     21        22        23        24        25        26        27        
                            28        29        30
                             31        32        33
</pre>

<p>An instance of the game begins with some holes having pegs in them and the rest of the holes being empty. The game proceeds by jumping one peg over another, either horizontally or vertically, with the peg that is jumping landing in an empty hole, and the peg being jumped over being removed from the board. For example, if 9 is empty and 10 and 11 are not, then the peg in 11 can be "moved" to 9 with the peg in 10 being removed. After this move, 10 and 11 would both be empty but 9 would have a peg in it.</p>

<p>Given a specific board configuration your program will pick and model a specific move, over and over, until no more moves are available. Your program will then report the sum of the holes that still have pegs in them. At any point during the game there may be more than one possible move available. In such a case always model the move with the target hole of the moving peg as large as possible. If there is more than one move available to the largest possible target hole, then choose from those moves the one with the larger source hole.</p>

<p>For example, if the board looks like this, with X representing a peg and O representing a hole:</p>

<pre>                                 O         O         O
                                 O         O         O
          O         O         O         X         O         X         O
          O         O         O         X         O         X         O
          O         O         O         O         X         O         O
                                 O         O         O
                                 O         O         O
</pre>

<p>then the following jumps would be made: 1: from 12 over 19 to 26 (26, 24, and 5 are the only possible targets and 26 is the largest), 2: from 26 to 24 over 25 (5 and 24 are the only possible targets with 24 > 5 plus 24 is the target for two possible moves, one from 26 and one from 10; the one from 26 is used since 26 > 10), 3: from 17 to 29 (29 > 5), and two pegs would be left, one in hole 10 and one in hole 29. Thus 39 would be reported as the result for this instance.</p>

<p>[NOTE: The above paragraph is wrong. This was discovered shortly after the contest began, and the correction was broadcast to all teams. The second jump should be from 25 to 27. The third jump should be from 10 to 24. The two pegs left will be in holes 24 and 27 and 51 should be reported as the result.]</p>

### 입력 

 <p>The first line contains an integer N between 1 and 10 describing how many instances of the game are represented.  The remaining lines will describe N instances of the game by listing the holes which begin with pegs in them, in increasing order.  A 0 will indicate the end of each  sequence of unique numbers between 1 and 33 that represents an instance of the game.</p>

### 출력 

 <p>There should be N+2 lines of output.  The first line of output will read HI Q OUTPUT. There will then be one line of output for each instance of the game, reporting the sum of the holes that still have pegs in them for the final configuration of that instance.. The final line of output should read END OF OUTPUT .</p>

