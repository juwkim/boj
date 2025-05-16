# [Silver I] Election Meddling - 18058 

[문제 링크](https://www.acmicpc.net/problem/18058) 

### 성능 요약

메모리: 115840 KB, 시간: 436 ms

### 분류

이분 탐색, 브루트포스 알고리즘, 매개 변수 탐색, 정렬

### 제출 일자

2025년 5월 17일 03:02:22

### 문제 설명

<p>Your university definitely needs a new building solely dedicated to computer science. The department has the money for it, but the city council does not want to approve the building permit for the new building. That’s unfortunate!</p>

<p>Luckily, council elections are right around the corner. You have decided to participate in that election with the Interest Council Party for Computer science (ICPC). Once you have a majority of the votes in the council, you and your party colleagues can approve the new building.</p>

<p>The council elections are held in a number of districts to which the voters are assigned. Each district elects one council member. Each party fields one candidate per district and every voter has only one vote. The candidate with the most votes in each district will be elected as a council member.</p>

<p>Since the new building is very important to you and your party colleagues, you don’t want to take any chances. In case of a tie in the council or in an election in a district no one knows what happens. So your objective is to win an outright majority in the council – i.e. strictly more than half of the members. Further, in each district you consider won, the ICPC candidate must receive strictly more votes than any other candidate.</p>

<p>You and your colleagues of the ICPC have created an incredibly sophisticated simulation of the election. Thus, you know exactly how many voters will vote for each candidate in every district. Sadly, your model does not predict a victory for the ICPC in the election. Here comes the tricky question: How many voters do you have to bribe at least in order to win the election? If you bribe a voter, he will change his previously preferred party (which you know due to your meticulous modelling) to the ICPC. People who didn’t want to vote cannot be bribed.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>One line with two integers w and p (2 ≤ w, p ≤ 1 000), the number of districts and the number of parties running in the election. The parties are numbered 1 to p and the ICPC is party 1.</li>
	<li>w lines, each with p integers v<sub>1</sub>, . . . , v<sub>p</sub> (0 ≤ v<sub>i</sub> ≤ 1 000 for each i) giving the projected results for a district. v<sub>i</sub> denotes the number of votes that will be cast for party i.</li>
</ul>

<p>It is guaranteed that there is at least one voter in each district, i.e. the sum of all v<sub>i</sub> per district will always be at least one.</p>

### 출력 

 <p>Output the minimum number of voters that have to be bribed in order for the ICPC to win a majority of the seats in the council.</p>

