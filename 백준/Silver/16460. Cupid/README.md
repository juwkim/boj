# [Silver IV] Cupid - 16460 

[문제 링크](https://www.acmicpc.net/problem/16460) 

### 성능 요약

메모리: 30840 KB, 시간: 84 ms

### 분류

구현(implementation), 정렬(sorting), 문자열(string)

### 문제 설명

<p>Since 1969, the Internet has upended all kind of industries - retailing, politics, entertainment, etc. Among them may its most profound repercussion well be—on how we choose a mate.</p>

<p>At the stage of its emergence, the notion of meeting someone via online seemed pathetic and freakish. However, now, it becomes a necessity for someone, especially who are coping with social or geographical constraints. In the United States, 70% of gay people meet their partner online. Other evidence also suggests that it contributes to breaking down homogeneous groups by boosting interracial and international marriage.</p>

<p>On the other hand, service providers are also coping with an inherent conflict of interests: the better matching for users, the fewer people left in the service. Thus, to keep a sustainable business model, the firms decided to provide premium services, such as "see who Liked me". With this, you can save a lot of time for answering yes or no for candidates who would not finally Like you, hence "not a match".</p>

<p>Now you only have to set your gender preference and maximum geographical distance. <em>(No long-distance relationship in the beginning!)</em> It is time to see your candidates.</p>

### 입력 

 <p>The name of a premium user, his or her gender preference, and maximum geographical distance are given, separated by a space, in the first line. The maximum geographical distance is an integer.  The gender preference is one of 'F', 'FM', 'M', and 'MF', representing user's preference about two traditional genders; female(denoted by 'F') and male(denoted by 'M'). Both 'FM' and 'MF' represent that the user prefers both genders.</p>

<p>In the second line, the number of users,  1 ≤ 𝑁 ≤ 100,000, is given. For next $N$ lines, the name of a user who liked the premium user, his or her gender(denoted by either 'F' or 'M'), and the geographical distance to the premium user are given in each line, separated by a space.</p>

<p>All the names consist only of alphabet characters and their length is not greater than 10. If there are duplicative names, print as many as they appear.</p>

<p>All the geographical distances and the user's limit of it are represented as an integer between 1 and 20,000 inclusive.</p>

### 출력 

 <p>Print the name of users who meet the gender preference and geographical condition of the premium user, in lexicographical order, line by line.</p>

<p>If there is no user who meets them, print "No one yet".</p>

