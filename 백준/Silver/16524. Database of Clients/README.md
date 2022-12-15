# [Silver IV] Database of Clients - 16524 

[문제 링크](https://www.acmicpc.net/problem/16524) 

### 성능 요약

메모리: 114328 KB, 시간: 156 ms

### 분류

자료 구조(data_structures), 구현(implementation), 파싱(parsing), 문자열(string), 트리를 사용한 집합과 맵(tree_set)

### 문제 설명

<p>Nowadays there are billions of email users. A little-known fact is that some email providers offer way more than the usual <code>username@provider.com</code> email address.</p>

<p>Some providers simply ignore dots in usernames. Thus, if John owns the username <code>johnsmith</code>, he could tell people that his email address is <code>johnsmith@provider.com</code>, <code>john.smith@provider.com</code> or <code>john.s.mith@provider.com</code>, among others. Emails sent to any of these addresses would end up on his mailbox.</p>

<p>Other providers allow appending the character “<code>+</code>” followed by any combination of letters and/or digits after the username. With this feature, by registering the username <code>johnsmith</code>, John would also be able to use <code>johnsmith+friends@provider.com</code> and <code>johnsmith+2x3is6@provider.com</code>.</p>

<p>Sometimes both features are available at once and in those cases <code>john.smith+icpc@provider.com</code> and <code>john.smith+wants.2.eat.lemon.3.14@provider.com</code> are valid addresses that John could use.</p>

<p>This is quite useful for users, who can manage different addresses to help organize their mailboxes and easily filter the newsletters eventually sent after registering on a new website. Unfortunately, this also opens up space for abuse. Some websites rely upon the fact that each email address identifies a single user. However, a misbehaving user might easily create multiple accounts by taking advantage of the multiple addresses allowed by the email provider.</p>

<p>After learning all of this your boss got really worried. What if the number of unique users that has been reported to the shareholders is not accurate, bloated by duplicate accounts instead? That brings you to the task at hand: given the list of all email addresses from the users database of the company, you must determine the real number of unique users, assuming that all email providers have both described features available.</p>

### 입력 

 <p>The first line contains an integer N (1 ≤ N ≤ 1000) representing the number of email addresses in the database. Each of the next N lines contains a string of at most 100 characters representing an email address in the database. Each email address has the form localpart@provider where localpart is a non-empty list of labels with a “<code>.</code>” (dot) or a “<code>+</code>” (plus sign) between each pair of consecutive labels, and provider is a non-empty list of labels always with a “.” (dot) between each pair of consecutive labels. A label is a non-empty sequence of lowercase letters and/or digits. The character “<code>+</code>” (plus sign) appears at most once in each email address.</p>

### 출력 

 <p>Output a single line with an integer indicating the number of unique users in the database.</p>

