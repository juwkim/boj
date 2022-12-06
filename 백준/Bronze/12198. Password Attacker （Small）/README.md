# [Bronze I] Password Attacker (Small) - 12198 

[문제 링크](https://www.acmicpc.net/problem/12198) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

브루트포스 알고리즘(bruteforcing), 조합론(combinatorics), 수학(math)

### 문제 설명

<p>Passwords are widely used in our lives: for ATMs, online forum logins, mobile device unlock and door access. Everyone cares about password security. However, attackers always find ways to steal our passwords. Here is one possible situation:</p>

<p>Assume that Eve, the attacker, wants to steal a password from the victim Alice. Eve cleans up the keyboard beforehand. After Alice types the password and leaves, Eve collects the fingerprints on the keyboard. Now she knows which keys are used in the password. However, Eve won't know how many times each key has been pressed or the order of the keystroke sequence.</p>

<p>To simplify the problem, let's assume that Eve finds Alice's fingerprints only occurs on <b>M</b> keys. And she knows, by another method, that Alice's password contains <b>N</b> characters. Furthermore, every keystroke on the keyboard only generates a single, unique character. Also, Alice won't press other irrelevant keys like 'left', 'home', 'backspace' and etc.</p>

<p>Here's an example. Assume that Eve finds Alice's fingerprints on <b>M</b>=3 key '3', '7' and '5', and she knows that Alice's password is <b>N</b>=4-digit in length. So all the following passwords are possible: 3577, 3557, 7353 and 5735. (And, in fact, there are 32 more possible passwords.)</p>

<p>However, these passwords are not possible:</p>

<pre>1357  // There is no fingerprint on key '1'
3355  // There is fingerprint on key '7',
         so '7' must occur at least once.
357   // Eve knows the password must be a 4-digit number.
</pre>

<p>With the information, please count that how many possible passwords satisfy the statements above. Since the result could be large, please output the answer modulo 1000000007(10<sup>9</sup>+7).</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <b>T</b>.</p>

<p>For the next <b>T</b> lines, each contains two space-separated numbers <b>M</b> and <b>N</b>, indicating a test case.</p>

### 출력 

 <p>For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1) and y is the total number of possible passwords modulo 1000000007(10<sup>9</sup>+7).</p>

