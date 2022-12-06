# [Bronze I] Vaccine Efficacy - 21205 

[문제 링크](https://www.acmicpc.net/problem/21205) 

### 성능 요약

메모리: 30840 KB, 시간: 488 ms

### 분류

사칙연산(arithmetic), 구현(implementation), 수학(math), 확률론(probability), 문자열(string)

### 문제 설명

<p>To determine the efficacy of a vaccine against a disease, a clinical trial is needed.  Some participants are given the real vaccine, while others are given a placebo as the control group.  The participants are tracked to determine if they are infected by three different strains (A, B, and C) of a virus.  The efficacy of the vaccine against infection by a particular strain is simply the percentage reduction of the infection rate of the vaccinated group compared to the control group.</p>

<p>For example, suppose that there are $40$ people in the vaccinated group, $8$ of which are infected by strain B.  Then the infection rate is $20$%.  Further suppose that $50$ people are in the control group, and $30$ people are infected by strain B.  Then the infection rate for the control group is $60$%.  Thus the vaccine efficacy against infection is approximately $66.67$% (since $20$% is a $66.67$% percentage reduction of $60$%).  If the infection rate for a particular strain in the vaccinated group is not lower than that of the control group, the vaccine is not effective against infection by that strain.</p>

<p>What is the vaccine efficacy against infection by the three strains?</p>

### 입력 

 <p>The first line of input contains an integer $N$ ($2 \leq N \leq 10\,000$) containing the number of participants in the clinical trial.</p>

<p>The next $N$ lines describe the participants. Each of these lines contains a string of length four. Each letter is either 'Y' or 'N'.  The first letter indicates whether the participant is vaccinated with the real vaccine, and the remaining three letters indicate whether the participant is infected by strain A, B, and C, respectively.</p>

<p>There is at least one participant in the vaccinated group and the control group.  There is at least one participant in the control group infected by each strain (but they may be different participants).</p>

### 출력 

 <p>Display the vaccine efficacy against infection by strain A, B, and C in that order.  If the vaccine is not effective against infection by a particular strain, display <code>Not Effective</code> for that strain instead.  Answers with an absolute error or relative error of at most $10^{-2}$ will be accepted.</p>

