# [Bronze III] Transactions - 2975 

[문제 링크](https://www.acmicpc.net/problem/2975) 

### 성능 요약

메모리: 28776 KB, 시간: 64 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math)

### 문제 설명

<p>Whenever somebody goes to an ATM to withdraw or deposit money, a calculation has to be done to keep the person's bank balance correct. Your task in this problem is to do such calculations. There is a bank rule that says that a customer may not have an overdraft of more than $200, so any withdrawal that would take the balance below –200 must be stopped. (A minus sign is used to indicate an overdraft, or negative balance).</p>

### 입력 

 <p dir="ltr">Input consists of a number of lines, each representing a transaction. Each transaction consists of an integer representing the starting balance (between –200 and +10,000), the letter W or the letter D (Withdrawal or Deposit), followed by a second integer representing the amount to be withdrawn or deposited (between 5 and 400). Input will be terminated by a line containing 0 W 0.</p>

### 출력 

 <p dir="ltr">Output consists of one line for each line of input showing the new balance for each valid transaction If a withdrawal would take the balance below -200, the output must be the words ‘Not allowed’.</p>

