# [Silver III] SHAKE - 4873 

[문제 링크](https://www.acmicpc.net/problem/4873) 

### 성능 요약

메모리: 120212 KB, 시간: 184 ms

### 분류

구현

### 제출 일자

2025년 3월 31일 13:03:14

### 문제 설명

<p>Sam wants to send secret messages to Sally, and visa versa, so they devise a simple but effective encryption scheme they can perform by hand. However, they soon begin to fall in love and their messages to each other are growing longer and longer. Therefore, they decide their encryption scheme needs to be automated. Your job is to write a computer program that will implement their "shake, rattle and roll" encryption scheme. (Decryption will not be implemented at this time.)</p>

<p>A text message is placed into a 2D array in row major order, with each character in a unique cell of the array. If the message does not totally fill the array, the empty cells are filled with the capital letters of the alphabet starting with the letter A and going thru the letter Z (repeated as needed). For example, the message, "Meet me at the pizza parlor" in a 6 by 6 array would look like the figure below. Note that all characters are stored as capital letters.</p>

<p><img alt="" src="https://upload.acmicpc.net/e3a2d36e-53a2-4595-b97a-3622948f36e4/-/preview/"></p>

<p>To encrypt this message, 3 separate operations are performed as follows:</p>

<p><b>Shake</b>: Each odd column is shifted up one character, with the top most character moving to the bottom of the column. Each even column is shifted down, with the bottom most chararacter moving to the top of the column. The columns are numbered starting at 1. For example:</p>

<p><img alt="" src="https://upload.acmicpc.net/1978413e-c8d4-4351-b7d5-8e772a1da634/-/preview/"></p>

<p><b>Rattle</b>: Each odd row is shifted to the right one character, with the rightmost character moving to the leftmost column in the same row. Each even row is shifted to the left one character, with the leftmost character moving to the rightmost column in the same row. The rows are numbered starting at 1 from the top. For example:</p>

<p><img alt="" src="https://upload.acmicpc.net/cd32c694-a818-46d6-9733-e17f3943381d/-/preview/"></p>

<p><b>Roll</b>: Each odd "loop" around the matrix is rotated to the right one character, while each even "loop" is rotated to the left one character, as shown in the figure below. "Loops" are even or odd based on the row number of their top most row (with the top row being row 1).</p>

<p><img alt="" src="https://upload.acmicpc.net/7a5763bd-7c04-4ef7-9be9-2ea01ccf17f2/-/preview/"></p>

<p>The matrix size is specified in the encryption key and can vary in size from 3x3 to 100x100. The matrix is always square.</p>

### 입력 

 <p>The input file will contain one or more encryption problems. Each problem takes up two lines of the file. The first line of a problem is the encryption key. The second line is the text to be encrypted. An encryption key always begins with a two digit matrix size, followed by a series of 'S', 'R', or L' characters in any order. For each 'S' character, a "shake" operation is performed, for each 'R' character a 'rattle" operation is performed, and for each 'L' character a "roll" operation is performed, in the order specified. A size of "00" is interpreted as 100.</p>

<p>The encryption key is limited to 80 characters. The message is limited to 10,000 characters. Assume that the message will always fit inside the specified matrix.</p>

### 출력 

 <p>Other than the standard header and trailer messages, the encrypted text is output for each problem. The length of the encrypted text is the size of the matrix squared (e.g., a 3x3 matrix produces a string of length 9).</p>

