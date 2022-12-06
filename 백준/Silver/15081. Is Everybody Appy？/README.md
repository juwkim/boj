# [Silver V] Is Everybody Appy? - 15081 

[문제 링크](https://www.acmicpc.net/problem/15081) 

### 성능 요약

메모리: 113112 KB, 시간: 120 ms

### 분류

자료 구조(data_structures), 해시를 사용한 집합과 맵(hash_set), 구현(implementation), 문자열(string), 트리를 사용한 집합과 맵(tree_set)

### 문제 설명

<p>Joyce Stick is a mother of several children and has strict rules on how much technology they can use. One of her rules is that each kid can have at most one app on their phone. While the kids aren’t thrilled with this rule, they know if they complain they will lose their half-hour a day TV privileges. In order to maximize the number of apps that they can share with each other they’ve decided that each kid will pick a different app. Of course, each kid likes different apps, and each wants the app they like best (or near best) to be the app on their phone. Here’s how they’ve decided to select the apps: each kid writes down the apps they like on a list, starting with the app they like the most to the app they like the least (and leaving off apps they have absolutely no interest in). Then the oldest kid gets to pick the first app on his/her list to put on their phone. The second oldest gets to pick the first app on their list, unless it’s already been picked by the oldest, in which case they get the second app on their list. This process repeats for each of the other kids – each gets the highest app on their list that hasn’t already been picked. Given a list of each kid’s app preferences, you must determine what app gets put on each phone.</p>

### 입력 

 <p>Input starts with a line containing a positive integer n (n ≤ 100), where n is the number of kids. Following this are n lines, each starting with a positive integer m (m ≤ 50) followed by m strings. The value of m indicates the number of apps on a kid’s list, and the m strings are the names of the apps, from most preferred to least preferred. The first line is the preference list of the oldest kid, the second line is the preference list for the second oldest, and so on. Length of the name of the apps does not exceed 10.</p>

### 출력 

 <p>Display the app selected for each kid’s phone, from oldest kid to youngest, separating each app’s name with a single blank. There will never be a test case where all of the apps on a kid’s list will have been selected by older kids.</p>

