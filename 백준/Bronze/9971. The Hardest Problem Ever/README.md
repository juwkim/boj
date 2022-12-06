# [Bronze II] The Hardest Problem Ever - 9971 

[문제 링크](https://www.acmicpc.net/problem/9971) 

### 성능 요약

메모리: 28776 KB, 시간: 72 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Julius Caesar lived in a time of danger and intrigue. The hardest situation Caesar ever faced was keeping himself alive. In order for him to survive, he decided to create one of the first ciphers. This cipher was so incredibly sound, that no one could figure it out without knowing how it worked. You are a sub captain of Caesar’s army. It is your job to decipher the messages sent by Caesar and provide to your general. The code is simple. For each letter in a plaintext message, you shift it five places to the right to create the secure message (i.e., if the letter is ‘A’, the cipher text would be ‘F’). Since you are creating plain text out of Caesar’s messages, you will do the opposite:</p>

<pre>Cipher text
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

Plain text
V W X Y Z A B C D E F G H I J K L M N O P Q R S T U</pre>

<p>Only letters are shifted in this cipher. Any non-alphabetical character should remain the same, and all alphabetical characters will be upper case.</p>

### 입력 

 <p>Input to this problem will consist of a (non-empty) series of up to 100 data sets. Each data set will be formatted according to the following description, and there will be no blank lines separating data sets. All characters will be uppercase.</p>

<p>A single data set has 3 components:</p>

<ol>
	<li>Start line – A single line, “START”</li>
	<li>Cipher message – A single line containing from one to two hundred characters, inclusive, comprising a single message from Caesar</li>
	<li>End line – A single line, “END”</li>
</ol>

<p>Following the final data set will be a single line, “ENDOFINPUT”.</p>

### 출력 

 <p>For each data set, there will be exactly one line of output. This is the original message by Caesar.</p>

