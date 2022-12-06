# [Bronze I] Safe Squares - 20721 

[문제 링크](https://www.acmicpc.net/problem/20721) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

구현(implementation)

### 문제 설명

<p>Penny is a young, enthusiastic pawn with significant ambitions. She hopes to improve her currently measly ranking and one day become queen of her entire chess board! Unfortunately, the current queen prefers the pawns of her kingdom do nothing but her bidding and views Penny's ambitions as a potential source of rebellion. She sends her loyal rooks onto the board to capture Penny and bring her before the royal court to face punishment.</p>

<p>Penny obviously does not want to be captured by the queen's rooks, but she does not know the safe spots on the board to escape to. If she goes to any square that is in the same row or same column as a rook, the rook will capture her! Given the locations of all the rooks, tell Penny how many squares there are on the chess board where she would be safe from the rooks!</p>

### 입력 

 <p>The input consists of $8$ lines that each contain exactly $8$ characters. Each line represents one row of the chessboard, and contains only <code>R</code> and <code>.</code> characters. The <code>R</code> characters are squares which contain a rook and the <code>.</code> characters represent empty squares.</p>

### 출력 

 <p>Print the number of squares on the chess board where Penny is safe from the rooks: where no rook is in the same row or column as the square. Note that there may be no safe squares (because the entire board is filled with rooks, or because every empty square is in the same row or column as a rook) in which case you should print <code>0</code>.</p>

