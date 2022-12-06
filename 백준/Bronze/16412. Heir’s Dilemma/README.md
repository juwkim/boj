# [Bronze II] Heir’s Dilemma - 16412 

[문제 링크](https://www.acmicpc.net/problem/16412) 

### 성능 요약

메모리: 28776 KB, 시간: 648 ms

### 분류

사칙연산(arithmetic), 브루트포스 알고리즘(bruteforcing), 수학(math), 문자열(string)

### 문제 설명

<p>Your favorite uncle has passed away, leaving you a large estate. Bank account numbers, locations of safe deposit boxes, and GPS coordinates to buried treasures are all locked in an electronic safe in your uncle’s office behind a picture of dogs playing poker. One day he showed you the safe with its 9 digit keypad (digits 1 through 9). He told you he wasn’t worried about anyone breaking into his safe because it’s equipped with a self-destruct mechanism that will destroy the contents if anyone attempts a forced entry.</p>

<p>The combination is a sequence of six decimal digits. If an incorrect combination is entered the safe enforces a thirty-second delay before accepting another combination. So a brute-force effort to try all six-digit combinations could take months.</p>

<p>Your uncle had planned to give you, his sole heir, the combination one day, but due to an unfortunate hanggliding accident in Kansas, you now must rely on your deductive and programming skills to access the key to your inheritance.</p>

<p>Here’s what you know:</p>

<ul>
	<li>The combination c is a sequence of six non-zero decimal digits.</li>
	<li>Your mother recalls that she heard your uncle mention that all the digits are different.</li>
	<li>You remember that your uncle once said that the six digit number was divisible by each of its individual digits.</li>
</ul>

<p>An example satisfying these conditions is 123864: all six digits differ, and you can check that 123864 is divisible by each of 1, 2, 3, 8, 6 and 4.</p>

<p>Even with the helpful data, it could take a while to get to open the safe, so the task is likely to be split into several sessions with separate ranges being tested. How many combinations are there to try in the range given?</p>

### 입력 

 <p>The input is a line with two space-separated integers L and H, where 123 456 ≤ L < H ≤ 987 654</p>

### 출력 

 <p>Print one integer, the total number of possible combinations to the safe, where each combination c must satisfy the three constraints above, and lie in the range L ≤ c ≤ H.</p>

