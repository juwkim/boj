# [Silver IV] Limit Checking - 2127 

[문제 링크](https://www.acmicpc.net/problem/2127) 

### 성능 요약

메모리: 112008 KB, 시간: 128 ms

### 분류

구현

### 제출 일자

2024년 3월 31일 21:24:02

### 문제 설명

<p>From time to time, customers of the First Goldfields Bank of Pembroke make dramatic errors with their banking transactions. For example, they might add an extra zero and transfer <span>$</span>10,000 to someone else when they only intended to transfer <span>$</span>1,000. The bank theorises that this is related to the large sums of money and large drinking budgets associated with a successful goldfield, and plans to introduce transaction limits to detect and prevent serious errors.</p>

<p>Each transaction is a request to transfer an amount of money from one account to another. There are two different kinds of transactions: if the transfer is between two accounts owned by the same customer, then it is an inter-account transfer (IAT); otherwise, when transferring money to someone else’s account, the transaction is known as a payment.</p>

<p>The bank has invited each customer to specify a maximum instruction limit and a daily exposure limit for each kind of transaction, with the expectation that most customers will want to set higher limits for inter-account transfers than for general payments.</p>

<p>These limits are applied as follows:</p>

<ul>
	<li>A transaction will fail if its value exceeds the applicable maximum instruction limit.</li>
	<li>A transaction will fail if the applicable daily exposure limit is exceeded when its value is added to the total value of the customer’s previously successful transactions of the same kind that day. (But later transactions might succeed if they are for smaller amounts.)</li>
</ul>

<p>Your task is to write the program to enforce these limits.</p>

### 입력 

 <p>Each line of the input file is a banking record, consisting of a number of fields separated by commas (‘,’). There are four types of banking record, distinguished by the first field:</p>

<ul>
	<li>'1’ records are customer records, which have six fields. The second field is the customer name, consisting of exactly eight uppercase letters. The remaining fields are amounts; from left to right they are the customer’s IAT maximum instruction limit, IAT daily exposure limit, general payment maximum instruction limit, and general payment daily exposure limit.</li>
	<li>‘2’ records are account records, which have three fields. The third field is the account number, consisting of exactly six digits (‘0’ to ‘9’). These records specify that the account is owned by the customer named by the second field.</li>
	<li>‘5’ records are instruction records and have a total of six fields, representing a transaction. The second through sixth fields are: the date of the transaction, in the format YYYYMMDDhhmmss; the customer making the transaction; the source account (from which the money is to come); the amount; and the destination account.</li>
	<li>The ‘9’ record terminates the input file, and has just one field.</li>
</ul>

<p>All amounts in the input data are dollars and cents values written with a decimal point (‘.’) and two cents digits (but no commas), with a maximum value of <span>$</span>9,999,999.99. All ‘1’ records appear before all ‘2’ records, which appear before all ‘5’ records, which appear before the ‘9’ record.</p>

<p>All customer names appearing in ‘2’ or ‘5’ records will be valid customers who have been listed in exactly one ‘1’ record, and all account numbers appearing in ‘5’ records will be valid accounts which have been listed in exactly one ‘2’ record. Furthermore, the ‘5’ records will appear in increasing datestamp order. There will be no more than 50 customers and 200 accounts.</p>

<p>The bank does not accept transactions between 23:00 and 06:00, believing that customers will be more than usually impaired during these periods—especially at weekends. Hence such times do not appear in the input file.</p>

### 출력 

 <p>Output must contain one line for each input ‘5’ record, starting with ‘INSTRUCTION n: ’, where n is the instruction number (starting from 1), followed by one of the following messages, as appropriate:</p>

<p>‘NOT OWNER’ if the source account is not owned by the customer;<br>
‘IAT MAX EXCEEDED’ or ‘PAYMENT MAX EXCEEDED’ if the transaction amount exceeds the applicable maximum instruction limit;<br>
‘IAT DEL EXCEEDED’ or ‘PAYMENT DEL EXCEEDED’ if the transaction amount would cause the applicable daily exposure limit to be exceeded;<br>
or ‘IAT OK’ or ‘PAYMENT OK’ if the transaction is successful.</p>

<p>If a transaction fails both limit tests, output only the ‘. . . MAX EXCEEDED’ message.</p>

