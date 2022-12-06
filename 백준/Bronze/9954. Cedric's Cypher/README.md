# [Bronze II] Cedric's Cypher - 9954 

[문제 링크](https://www.acmicpc.net/problem/9954) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>A Caesar cipher is a way of encrypting text. Each letter in the text is replaced by the letter s places after it in the alphabet. S is called the shift – with a shift of 5, for example, 'A' becomes 'F', 'H' becomes 'M' and 'Y' becomes 'D '(the alphabet wraps round so 'A' follows 'Z'). The text is easy to decrypt if you know the value of s.</p>

<p>Cedric has come up with a variation on this. Instead of telling his friends what the shift is, he encrypts the letter 'A' (always producing an upper case letter) and places it at the end of his message. In that way, they can work out what the shift is and thus decrypt the text.</p>

### 입력 

 <p>Input will consist of a number of lines of text, terminated by a line consisting of only #. Each line will consist of up to 255 characters of encrypted text (including the encrypted 'A').</p>

### 출력 

 <p>Output will be one line for each line of input containing the decrypted text. The final letter 'A' should NOT be included. Punctuation, spaces, digits and any other non-letter characters are output unchanged.</p>

