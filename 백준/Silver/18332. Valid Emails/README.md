# [Silver IV] Valid Emails - 18332 

[문제 링크](https://www.acmicpc.net/problem/18332) 

### 성능 요약

메모리: 114328 KB, 시간: 128 ms

### 분류

파싱(parsing), 문자열(string)

### 문제 설명

<p>This year, many people registered for the internet contest with several email addresses. We want to see how many valid and distinct email addresses registered.</p>

<p>A valid email address consists of a username and a domain name separated by a character ‘<code>@</code>’. A username is a string containing letters (<code>a-z</code> and <code>A-Z</code>), digits (<code>0-9</code>), underscores (<code>_</code>), and periods (<code>.</code>). Usernames cannot begin or end with a period and cannot contain two consecutive periods. Other than this rule, periods do not matter in email addresses (they can be removed without changing the address). Uppercase and lowercase letters in the usernames are considered the same. So, usernames <code>AliBaba</code> and <code>ali.baba</code> are considered the same. Usernames should contain 6 to 30 characters, after removing all of its periods.</p>

<p>A valid domain name is a string of length between 3 and 30 (inclusive), consisting of domain parts separated by periods (<code>.</code>). A domain name must not start or end with a period. Each domain part is a non-empty string of letters (<code>a-z</code> and <code>A-Z</code>), digits (<code>0-9</code>), and dash (<code>-</code>). Uppercase and lowercase letters in the domain names are also considered the same. So, <code>Foo.bar</code> is the same as <code>foo.Bar</code>, but not the same as <code>Foo-Bar</code> or <code>Foobar</code>.</p>

### 입력 

 <p>The first line of the input contains a positive integer n (1 ⩽ n ⩽ 1000), the number of the registered email addresses. Each of the next n lines contains one email address of length at most 100 and consisting of alphabets, digits, ‘<code>@</code>’, ‘<code>.</code>’, ‘<code>_</code>’, and ‘<code>-</code>’.</p>

### 출력 

 <p>Print a single integer which is the number of distinct email addresses that are valid.</p>

