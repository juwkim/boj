# [Bronze I] Guessing Game I - 6997 

[문제 링크](https://www.acmicpc.net/problem/6997) 

### 성능 요약

메모리: 28776 KB, 시간: 72 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>After a long trek through treacherous mountains, Bilbo and the dwarfs have arrived at the West Gate of the mines of <em>Puzzlia</em>, constructed by a mathematically inclined Dwarf King. The gate is of course not open (nothing can be that easy for our heroes), and Dwalin explains to Bilbo that they need to guess a 4-digit number (let’s call it “secret”) correctly to open the gate. He points out 8 geometrical shapes on top of the gate, 4 circles and 4 squares. Every time a guess is made (by standing in front of the gate and speaking each of the digits loudly), some of the squares and the circles will light up. If the guess is correct, then the gate will open; but if the number is not guessed correctly in 10 attempts, then... well, best not to think of such things.</p>

<p>Dwalin explains the rules about how the circles and squares will light up. Let <em>guess</em> denote a guess that is made. For every digit in <em>guess</em>: (1) if it is equal to the corresponding digit in <em>secret</em> (at the same position), then a circle will light up; (2) if it is equal to some digit in <em>secret</em> but at a different position, a square will light up. For example:</p>

<ul>
	<li><strong>secret</strong> = 1234, <strong>guess</strong> = 1357: The “1” in <em>guess</em> gives us one circle, whereas the “3” in <em>guess</em> gives us one square. The other two digits in <em>guess</em> do not have a match.</li>
</ul>

<p>The secret (and the guess) may contain duplicate digits. The rule for handling duplicates is simple: a digit in secret can only match one digit in guess (and vice versa), and exact matches supersede out-of-position matches. So we first check for exact matches, and then look for the second type.</p>

<ul>
	<li><strong>secret</strong> = 1234, <strong>guess</strong> = 1122: There is only one exact match, for position 1 (that gives us one circle). The second “1” in guess doesn’t match anything in secret (since the “1” in secret is already matched). Then, we get one square for the first “2” in guess, and that’s it.</li>
	<li><strong>secret</strong> = 1311, <strong>guess</strong> = 1122: One circle for exact match at position 1, and one square for an out-of-position match for digit “1”.</li>
	<li><strong>secret</strong> = 0011, <strong>guess</strong> = 0213: Two circles, no squares.</li>
</ul>

<p>Before trying to guess the secret of the gate, Bilbo would like to make sure he understands the process and develops some strategy. He would like your help with this. Specifically, he would like you to write a program that, given two numbers, tells him how many circles and squares would light up.</p>

### 입력 

 <p>The first line in the test data file contains the number of test cases (< 100). After that, each line contains one test case: the first number is the <em>secret</em> (provided as an int), and the following number is the <em>guess</em> (provide as an int). Both the numbers are ≤ 9999. Note that the numbers need to be padded with 0’s. For example, if one of the numbers is 1, it needs to be treated as 0001.</p>

### 출력 

 <p>For each test case, you are to output the numbers of circles and squares that will light up. Exact format shown below.</p>

