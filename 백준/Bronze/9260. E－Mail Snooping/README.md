# [Bronze I] E-Mail Snooping - 9260 

[문제 링크](https://www.acmicpc.net/problem/9260) 

### 성능 요약

메모리: 30840 KB, 시간: 232 ms

### 분류

구현(implementation), 파싱(parsing), 문자열(string)

### 문제 설명

<p>While there have been some claims — possibly false — that the government has only been logging meta-data for phone calls (and not actually listening in), such claims have been curiously absent for processing of e-mails. It is probably a good bet that the NSA is recording most e-mails, and that the main reason for not recording all phone calls may just be storage or other technological limitations (such as no direct access, only via data shared by phone carriers). Of course, the sheer volume of e-mails makes it impossible to read them all by hand, so a lot of text analysis will be carried out by algorithms. And as we all know, algorithms are fallible, so mistakes are bound to happen. (In fact, sending or receiving this problem set may very well put some of us or you on some watchlists.)</p>

<p>Here, we are going to look at a very simple version of e-mail processing. We assume that each e-mail consists only of words made up of lower-case letters, commas, periods, and spaces (space, tab, newline). There is a list of keywords that raise alarms. If at least a certain number of keywords occur in the text (at least once each), then the e-mail raises an alarm. You are to write a program that determines which e-mails raise alarms.</p>

### 입력 

 <p>The first line is the number K of input data sets, followed by the K data sets, each of the following form:</p>

<p>The first line contains three integers n, k, t, separated by spaces. 1 ≤ n ≤ 100 is the number of words that raise alarms; 1 ≤ k ≤ 100 is the number of lines in the e-mail that follows, and 1 ≤ t ≤ 100 is the number of keywords that need to occur to raise an alarm.</p>

<p>This is followed by n lines, each containing a word of at most 20 lowercase letters (and no other characters). Next come k lines, each containing at most 80 characters, a mix of lowercase letter, commas, periods, and different forms of spaces. No words will break across lines (a newline character ends a word, and a new word starts on the next line). We are only looking for exact matches, so “contest” and “contests” do not match.</p>

### 출력 

 <p>For each data set, output “Data Set x:” on a line by itself, where x is its number. Then, output either “Alarm” or “No Alarm”, depending on whether the the number of distinct keywords in the e-mail meets (or exceeds) the threshold or not. This should be followed by an empty line.</p>

