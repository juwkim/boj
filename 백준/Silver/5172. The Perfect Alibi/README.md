# [Silver IV] The Perfect Alibi - 5172 

[문제 링크](https://www.acmicpc.net/problem/5172) 

### 성능 요약

메모리: 110404 KB, 시간: 120 ms

### 분류

구현

### 제출 일자

2023년 11월 4일 06:07:49

### 문제 설명

<p>One of the more important things for a criminal to have (besides a weapon, a fast car, an army of martial arts freaks, and an entourage) is an alibi: a confirmation that the person was seen in a different place at the time the crime happened. That rules the criminal out as a suspect.</p>

<p>An alibi is usually of the form that some witness says “I saw him/her in place X from time Y to Z.” If the time range includes the time of the crime, and the police have no reason to mistrust the witness, this would prove that the suspect could not have committed the crime. Why would we mistrust a witness? For one, because some other witness claims that the same person was in another place during an overlapping time window. Here, we consider this as the only reason to mistrust a witness. Any witness who is not trusted is completely discarded. To be more precise, if two witnesses A and B claim to have seen the same suspect X in different places during time intervals which overlap, then we treat the input as though A and B never existed. (Of course, untrustworthy witnesses don’t prove guilt.)</p>

<p>You are to write a program to narrow down an initial set of suspects by using alibis given by witnesses, but discounting all untrustworthy witnesses.</p>

### 입력 

 <p>The first line contains the number K of data sets. This is followed by K data sets, each of the following form:</p>

<p>The first line contains four numbers s,w,p,t. 1 ≤ s ≤ 50 is the number of suspects, 1 ≤ w ≤ 200 the number of witnesses, 1 ≤ p ≤ 50 the number of possible locations, and 0 ≤ t ≤ 1000 the time of the crime (all are integers).</p>

<p>This is followed by w lines, each describing one witness statement by giving four numbers Si,Pi,bi,fi. 1 ≤ Si ≤ s is the number of the suspect the witness claims to have seen, 1 ≤ Pi ≤ p the place at which the witness claims to have been, and [bi,fi] the claimed time interval of the observation. All these numbers are integers.</p>

### 출력 

 <p>For each data set, output “Data Set x:” on a line by itself, where x is its number. On the subsequent lines, output, one per line, the suspects who are still under suspicion, i.e., the ones without valid alibis. If all suspects have alibis, output “No suspect.” instead. They should be output in sorted order. Each data set should be followed by an empty line.</p>

