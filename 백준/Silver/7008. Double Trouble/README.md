# [Silver I] Double Trouble - 7008 

[문제 링크](https://www.acmicpc.net/problem/7008) 

### 성능 요약

메모리: 114100 KB, 시간: 336 ms

### 분류

브루트포스 알고리즘, 구현, 문자열

### 제출 일자

2025년 6월 23일 01:06:33

### 문제 설명

<p>Alice Catherine Morris and her sister Irene Barbara frequently send each other e-mails. Ever wary of interceptions and wishing to keep their correspondence private, they encrypt their messages in two steps. After removing all nonalphabetic characters and converting all letters to upper case, they: 1)replace each letter by the letter s positions after it in the alphabet (1 <= s <= 25)|we call this a shift by s-and then, 2) divide the result of step 1 into groups of m letters and reverse the letters in each group (5 <= m <= 20). If the length of the message is not divisible by m, then the last k (less than m) letters are reversed. For example, suppose s = 2 and m = 6. If the plaintext were <br>
Meet me in St. Louis, Louis. after removing unwanted characters and changing to upper case we get </p>

<p>MEETMEINSTLOUISLOUIS </p>

<p>We will call this the modified plaintext. We then shift each letter by 2 (Y would be replaced with A and Z would be replaced by B, here), getting the intermediate result: </p>

<p>OGGVOGKPUVNQWKUNQWKU </p>

<p>And finally reverse every group of 6 letters: </p>

<p>GOVGGOQNVUPKWQNUKWUK </p>

<p>Note the last two letters made up the last reversed group. As is customary, we write the result in groups <br>
of 5 letters. So the ciphertext would be: </p>

<p>GOVGG OQNVU PKWQN UKWUK </p>

<p>Alas, it's not so hard to find the values for s and m when the ciphertext is intercepted. In fact it's even easier if you know a crib, which is a word in the modified plaintext. In the above example, LOUIS would be a crib. Your job here is to find s and m when presented with a ciphertext and a crib.</p>

### 입력 

 <p>Input will consist of multiple problem instances. The first line of input will contain a positive integer indicating the number of problem instances. The input for each problem will consist of multiple lines. The first line of input for a problem will contain the integer n (20 <= n <= 500) which is equal to the number of characters in the ciphertext. The following lines will contain the ciphertext, all upper case in groups of 5 letters separated by a single space. (The last group of letters may contain fewer than 5 letters.) There will be 10 groups of letters per line, except possibly for the last line of ciphertext. The input line following the last line of ciphertext will contain the crib; a single word consisting of between 4 and 10 (inclusive) upper case characters.</p>

### 출력 

 <p>Output will be two integers, s and m on a line, separated by a single space, indicating the encryption key that produces the crib, where s is the shift and m is the reversed group size. If there is more than one solution, output the one with smallest s. If there is more than one with the same s, output the one with smallest m. If no such s and m exist, output the message Crib is not encrypted.</p>

