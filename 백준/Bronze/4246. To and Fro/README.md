# [Bronze I] To and Fro - 4246 

[문제 링크](https://www.acmicpc.net/problem/4246) 

### 성능 요약

메모리: 30840 KB, 시간: 68 ms

### 분류

Empty

### 문제 설명

<p>Mo and Larry have devised a way of encrypting messages. They first decide secretly on the number of columns and write the message (letters only) down the columns, padding with extra random letters so as to make a rectangular array of letters. For example, if the message is “There’s no place like home on a snowy night” and there are five columns, Mo would write down</p>

<pre>t o i o y
h p k n n
e l e a i
r a h s g
e c o n h
s e m o t
n l e w x
</pre>

<p>Note that Mo includes only letters and writes them all in lower case. In this example, Mo used the character ‘x’ to pad the message out to make a rectangle, although he could have used any letter.</p>

<p>Mo then sends the message to Larry by writing the letters in each row, alternating left-to-right and right-to-left. So, the above would be encrypted as</p>

<p>toioynnkpheleaigshareconhtomesnlewx</p>

<p>Your job is to recover for Larry the original message (along with any extra padding letters) from the encrypted one.</p>

### 입력 

 <p>There will be multiple input sets. Input for each set will consist of two lines. The first line will contain an integer in the range 2 . . . 20 indicating the number of columns used. The next line is a string of up to 200 lower case letters. The last input set is followed by a line containing a single 0, indicating end of input.</p>

### 출력 

 <p>Each input set should generate one line of output, giving the original plaintext message, with no spaces.</p>

