# [Bronze I] Account Numbers - 20350 

[문제 링크](https://www.acmicpc.net/problem/20350) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Organising programming contests is a lot of work.  One of the many tasks, some say the most important one, is to arrange reimbursement for the jury (and other volunteers) for their travel to the contest. In order to obtain their reimbursements, the jury members provide (among other things) their <em>International Bank Account Number</em>s (IBANs), uniquely identifying their bank accounts.  If they make a typo when writing their IBAN, the reimbursement cannot be sent, but fortunately an IBAN contains two check digits that can be used to mitigate such errors.  Let us help the contest organisers by verifying that a provided IBAN is correct, so that the reimbursements are not delayed more than necessary.</p>

<p>For those of you who do not know, an IBAN is a string consisting of between $15$ and $34$ upper-case letters and digits.  To validate a given IBAN, the following amazing procedure is used. </p>

<ol>
	<li>Move the first four characters to the end of the string. </li>
	<li>Replace each letter by digits, where $A = 10$, $B = 11$, ..., $Z = 35$.</li>
	<li>Interpret the resulting string as a decimal number and compute the remainder modulo $97$. An IBAN is valid if and only if the remainder is $1$. </li>
</ol>

<p>For example, consider the IBAN "<code>NL20INGB0001234567</code>".  After performing the first step we get the string "<code>INGB0001234567NL20</code>", and then after replacing letters with digits we get the number $182316110001234567232120$.  The remainder of this number modulo $97$ equals $1$, so this was indeed a valid IBAN.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>One line with a string $s$ ($15 \leq \mathrm{length}(s) \leq 34$): the IBAN to validate. The IBAN only contains upper case letters and digits.</li>
</ul>

### 출력 

 <p>If the given IBAN is valid, output "<code>correct</code>".  Otherwise, output "<code>incorrect</code>".</p>

