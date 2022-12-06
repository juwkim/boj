# [Silver IV] Help Me with the Game - 6666 

[문제 링크](https://www.acmicpc.net/problem/6666) 

### 성능 요약

메모리: 113112 KB, 시간: 104 ms

### 분류

구현(implementation), 파싱(parsing), 정렬(sorting), 문자열(string)

### 문제 설명

<p>Your task is to read a picture of a chessboard position and print it in the chess notation.</p>

### 입력 

 <p>The input consists of an ASCII-art picture of a chessboard with chess pieces on positions described by the input. The pieces of the white player are shown in upper-case letters, while the black player's pieces are lower-case letters. The letters are one of "<code>K</code>" (King), "<code>Q</code>" (Queen), "<code>R</code>" (Rook), "<code>B</code>" (Bishop), "<code>N</code>" (Knight), or "<code>P</code>" (Pawn). The chessboard outline is made of plus ("<code>+</code>"), minus ("<code>-</code>"), and pipe ("<code>|</code>") characters. The black fields are filled with colons ("<code>:</code>"), white fields with dots ("<code>.</code>").</p>

### 출력 

 <p>The output consists of two lines. The first line consists of the string "<code>White: </code>", followed by the description of positions of the pieces of the white player. The second line consists of the string "<code>Black: </code>", followed by the description of positions of the pieces of the black player.</p>

<p>The description of the position of the pieces is a comma-separated list of terms describing the pieces of the appropriate player. The description of a piece consists of a single upper-case letter that denotes the type of the piece (except for pawns, for that this identifier is omitted). This letter is immediatelly followed by the position of the piece in the standard chess notation -- a lower-case letter between "<code>a</code>" and "<code>h</code>" that determines the column ("<code>a</code>" is the leftmost column in the input) and a single digit between 1 and 8 that determines the row (8 is the first row in the input).</p>

<p>The pieces in the description must appear in the following order: King("<code>K</code>"), Queens ("<code>Q</code>"), Rooks ("<code>R</code>"), Bishops ("<code>B</code>"), Knights ("<code>N</code>"), and pawns. Note that the numbers of pieces may differ from the initial position because of capturing the pieces and the promotions of pawns. In case two pieces of the same type appear in the input, the piece with the smaller row number must be described before the other one if the pieces are white, and the one with the larger row number must be described first if the pieces are black. If two pieces of the same type appear in the same row, the one with the smaller column letter must appear first.</p>

