# [Bronze I] Encrypted SMS - 6260 

[문제 링크](https://www.acmicpc.net/problem/6260) 

### 성능 요약

메모리: 30840 KB, 시간: 76 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>This year, ACM scientific committee members use emails to discuss about the problems and edit the selected ones. They know that email is not a secure way of communication, especially on such an important topic. So they transfer password-protected compressed file among themselves. In order to send the passwords, they use SMS. To increase the security level, the encrypted passwords are sent by SMS. To do this, a multi-tap SMS typing method is used.</p>

<p>Multi-tap is currently the most common text input method for mobile phones. With this approach, the user presses each key one or more times to obtain the wanted characters. For example, the key 2 is pressed once to get character A, twice for B, and three times for C.</p>

<p>The encryption algorithm that is used is quite simple: to encrypt the i th character of the password, the key used to obtain that character is tapped i more times. For if the 4th character of password is U, the key 8 is tapped 6 times, getting the character V. Note that to make the problem simple, we have assumed that the keypad does not generate digits.</p>

<p>The scientific committee needs a program to decrypt the received passwords. They are too busy to write this program and have asked you to help! Write a program to get a correct encrypted text and print the original password.</p>

<p style="text-align: center;"><img alt="" src="" style="height:215px; width:229px"></p>

<p style="text-align: center;">The standard 12 key telephone keypad</p>

### 입력 

 <p>The input consists of multiple test cases. Each test case contains a non-empty string of length at most 100, consisting of small or capital English letters. The last line of the input contains a single #.</p>

### 출력 

 <p>For each test case, write the decrypted password in a separate line. Note that passwords are case-sensitive.</p>

