# [Silver II] Email Destruction - 16652 

[문제 링크](https://www.acmicpc.net/problem/16652) 

### 성능 요약

메모리: 110064 KB, 시간: 112 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 파싱, 문자열

### 제출 일자

2024년 12월 16일 04:14:12

### 문제 설명

<p>You have an account on ICPCorrespondence.com. This is an email service where emails are grouped into chains by their subject as follows.</p>

<p>The first email in every chain has a non-empty subject consisting of lowercase English letters. Every succeeding email in the chain has a subject consisting of “<code>Re: </code>” followed by the subject of the previous email.</p>

<p>For example, if the first email in the chain has subject “<code>subj</code>”, then the second email has subject “<code>Re: subj</code>”, the third one has subject “<code>Re: Re: subj</code>”, and so on. Formally, the subject of the k-th email in the chain consists of “<code>Re: </code>” repeated k − 1 times followed by the subject of the first email in the chain.</p>

<p>In your mailbox, you had one or more chains of emails with unique subjects. You never removed any emails from your mailbox.</p>

<p>Unfortunately, one day ICPCorrespondence.com was attacked by hackers. As a result of this attack, some emails were removed from the server, while the remaining emails were shuffled.</p>

<p>You are not sure how many emails you had in the mailbox before the attack, but you guess that this number is n. Can you check whether this guess can be correct?</p>

### 입력 

 <p>The first line of the input contains two integers n and k — the number of emails that you think were in the mailbox before the attack, and the number of emails left after the attack, respectively (1 ≤ k ≤ n ≤ 100).</p>

<p>The following k lines contain subjects of the emails left in your mailbox, one per line. The subject of each email consists of “<code>Re: </code>” repeated zero or more times, followed by at least one and no more than 10 lowercase English letters. The length of each subject does not exceed 500. All email subjects are pairwise distinct.</p>

### 출력 

 <p>If your guess about the number of emails in your mailbox prior to the attack can be correct, output a single word “YES”. Otherwise, output a single word “NO”.</p>

