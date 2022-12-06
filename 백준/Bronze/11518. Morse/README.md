# [Bronze I] Morse - 11518 

[문제 링크](https://www.acmicpc.net/problem/11518) 

### 성능 요약

메모리: 30840 KB, 시간: 76 ms

### 분류

자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 구현(implementation), 문자열(string)

### 문제 설명

<p>A code developed by Samuel Morse was first used as a method of electronic communication between two operators sending long and short electrical impulses. These impulses would activate an armature equipped with an electromagnet. The duration of the impules and the silence between them evolved into what is now known as Morse Code.</p>

<p>Letters are represented with a series of dots and/or dashes.  SOS, the universal distress call, is represented by <code>... --- ...</code> (S = <code>...</code> and O = <code>---</code>). Typically, letters are separated by long pauses between them, otherwise they cannot be properly distinguished. Without the proper pauses, the code gets obfuscated.</p>

<p>The word ACM is represented in Morse Code by <code>.- -.-. --</code>, but ANY is represented by <code>.- -. -.--</code> and without the spacing between code letters, the words ACM and ANY are indistinguishable (<code>.--.-.--</code>).</p>

### 입력 

 <p>Input consists of the morse code conversion followed by a dictionary of valid words, then a number of test cases with words in morse code.</p>

<p>The first 26 lines of input each contain a unique upper case letter, a single space, and the morse code equivalent. The letters are in alphabetical order. The morse code equivalents will be exactly the same as the ones below in Sample Input.</p>

<p>The next line contains the number of valid words, N (1 <= N <= 100). The following N lines each contain a word containing 1 to 100 uppercase letters.</p>

<p>The dictionary is followed by one or more test cases. Each begins with a line containing the number of code words W (1 <= W <= 100) or 0 (zero) indicating end of input. The following W lines each contain a code word, in morse code, with no spacing between individual code letters. Each code word will contain 1 to 400 <code>.</code> and/or <code>-</code> symbols. If a codeword matches a word in the dictionary, it will only match a single word in the dictionary.</p>

### 출력 

 <p>For each test case, if all of the codewords are found in the dictionary, print a line containing the corresponding alphabetical word of each code word in a sentence on one line with each word separated by a single space. If any codeword in the input does not appear in the dictionary, report only the first such codeword followed by " not in dictionary." and do not print any corresponding alphabetical words.</p>

