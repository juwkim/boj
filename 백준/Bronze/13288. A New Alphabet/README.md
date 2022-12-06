# [Bronze II] A New Alphabet - 13288 

[문제 링크](https://www.acmicpc.net/problem/13288) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>A New Alphabet has been developed for Internet communications. While the glyphs of the new alphabet don’t necessarily improve communications in any meaningful way, they certainly make us feel cooler.</p>

<p>You are tasked with creating a translation program to speed up the switch to our more elite New Alphabet by automatically translating ASCII plaintext symbols to our new symbol set.</p>

<p>The new alphabet is a one-to-many translation (one character of the English alphabet translates to anywhere between 1 and 6 other characters), with each character translation as follows:</p>

<p><img alt="" src="" style="height:258px; width:630px"></p>

<p>For instance, translating the string “Hello World!” would result in:</p>

<p>[-]3110 \/\/0|Z1|)!</p>

<p>Note that uppercase and lowercase letters are both converted, and any other characters remain the same (the exclamation point and space in this example).</p>

### 입력 

 <p>Input contains one line of text, terminated by a newline. The text may contain any characters in the ASCII range 32–126 (space through tilde), as well as 9 (tab). Only characters listed in the above table (A–Z, a–z) should be translated; any non-alphabet characters should be printed (and not modified). Input has at most 10 000 characters.</p>

### 출력 

 <p>Output the input text with each letter (lowercase and uppercase) translated into its New Alphabet counterpart.</p>

