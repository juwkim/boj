# [Bronze I] What’s on the Grille? - 11771 

[문제 링크](https://www.acmicpc.net/problem/11771) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>The grille cipher is a technique that dates back to 1550 when it was first described by Girolamo Cardano. The version we’ll be dealing with comes from the late 1800’s and works as follows. The message to be encoded is written on an n × n grid row-wise, top to bottom, and is overlaid with a card with a set of holes punched out of it (this is the grille).</p>

<p>The message is encrypted by writing down the letters that appear in the holes, row by row, then rotating the grille 90 degrees clockwise, writing the new letters that appear, and repeating this process two more times. Of course the holes in the grille must be chosen so that every letter in the message will eventually appear in a hole (this is actually not that hard to arrange).</p>

<p>An example is shown below, where the message “Send more monkeys” is encrypted as “noeesrksdmnyemoj”, after adding a random letter to fill out the grid (this example corresponds to the first sample input.)</p>

<p style="text-align: center;"><img alt="" src="" style="height:118px; width:516px"></p>

<p style="text-align: center;">Figure I.1</p>

<p>If the message is larger than the n × n grid, then the first n<sup>2</sup> letters are written in the grid and encrypted, then the next n<sup>2</sup> are encrypted, and so on, always filling the last grid with random letters if needed. Here, we will only be dealing with messages of length n<sup>2</sup>.</p>

<p>Your job, should you choose to accept it, is to take an encrypted message and the corresponding grille and decrypt it. And we’ll add one additional twist: the grille given might be invalid, i.e., the holes used do not allow every location in the grid to be used during the encryption process. If this is the case, then you must indicate that you can’t decrypt the message.</p>

### 입력 

 <p>The input starts with a line containing a positive integer n ≤ 10 indicating the size of the grid and grille. The next n lines will specify the grille, using ‘.’ for a hole and ‘X’ for a non-hole. Following this will be a line containing the encrypted message, consisting solely of lowercase alphabetic characters. The number of characters in this line will always be n<sup>2</sup>.</p>

### 출력 

 <p>Output the decrypted text as a single string with no spaces, or the phrase “invalid grille” if the grille is invalid.</p>

