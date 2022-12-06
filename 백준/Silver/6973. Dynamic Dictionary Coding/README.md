# [Silver IV] Dynamic Dictionary Coding - 6973 

[문제 링크](https://www.acmicpc.net/problem/6973) 

### 성능 요약

메모리: 113112 KB, 시간: 136 ms

### 분류

자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 파싱(parsing), 문자열(string)

### 문제 설명

<p>A common method of data compression, "dictionary coding", is to replace words in a text by numbers indicating their positions in a dictionary. Static dictionary coding, in which the dictionary is known in advance, can be problematic, as it is necessary to have the dictionary available to understand the coded text. Dynamic dictionary coding avoids this problem by deriving the dictionary from the text to be compressed. The text is processed from beginning to end, starting with an empty dictionary. Whenever a word is encountered that is in the dictionary, it is replaced by a number indicating its position in the dictionary. Whenever a word is encountered that is not in the dictionary, it appears as-is in the compressed text and is added to the end of the dictionary.</p>

<p>You are to implement dynamic dictionary coding.</p>

### 입력 

 <p>The first line of the input file contains a positive integer which is the number of sets of text which are to be compressed. Each set of text will consist of several lines containing text made of lower case letters and spaces only. You may assume that no word is longer than 20 letters, that no input line is longer than 80 characters, and that there are no more than 100 input lines. The sets of text are separated by a single blank line, and are to be compressed individually.</p>

### 출력 

 <p>The output file should contain the sets of text input compressed using dynamic dictionary coding as described above. Lineation and spacing should be preserved exactly as in the input file with the different sets of compressed text separated by a single blank line.</p>

