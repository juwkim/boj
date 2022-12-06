# [Bronze I] General Knight - 20574 

[문제 링크](https://www.acmicpc.net/problem/20574) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

Empty

### 문제 설명

<p>For the uninitiated, chess is a board game is played on a grid of $8 \times 8$ squares. The rows are numbered $1$ to $8$ with row $1$ at the bottom and columns are labeled with lowercase $a$ to $h$. The label of a square is its column, then its row. For example, valid square labels are $a1$ and $e5$.</p>

<p>In chess, a piece <em>threatens</em> a square on the board if the piece can move to that square in one move. The knight is one of the more fearsome chess pieces, as it moves differently from the other pieces. In a single move, a knight can move two rows and one column or one column and two rows. The image below shows the squares a standard chess knight threatens if it starts in square $e5$.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 512px; height: 522px;"></p>

<p>The standard chess knight is a $(2, 1)$-knight. The more general version is an $(a, b)$-knight, which in one move can move either $a$ rows and $b$ columns, or $b$ rows and $a$ columns. Citizens of the chessboard are concerned, as they don't know how powerful these new knights are. Given an $(a, b)$-knight and its starting square, which squares does it threaten?</p>

### 입력 

 <p>Input consists of two lines. The first line has two space-separated integers $a$ and $b$, the properties of the knight. It is guaranteed that $0 \leq a, b < 8$ and $\max(a, b) > 0$. The second line contains the starting location of the $(a, b)$-knight. This is given in standard chess notation as described above.</p>

### 출력 

 <p>First, output an integer $k$, the number of squares the knight can reach. On the second line, output $k$ space separated strings, the positions the knight can move to in exactly one move. Sort these positions in increasing column order, breaking ties by increasing row.</p>

