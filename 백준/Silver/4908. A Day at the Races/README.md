# [Silver II] A Day at the Races - 4908 

[문제 링크](https://www.acmicpc.net/problem/4908) 

### 성능 요약

메모리: 112300 KB, 시간: 112 ms

### 분류

구현, 정렬

### 제출 일자

2025년 3월 16일 08:27:00

### 문제 설명

<p>Formula One is the highest class of car racing sports. A typical Formula One season consists of a series of races called “Grands Prix” which constructors like Ferrari, Renault, etc. and others participate with one or more cars driven by the best drivers in the world. During the season, teams compete in two parallel championships: the drivers championship and the teams championship.</p>

<p>In the drivers championship, drivers compete to achieve the maximum total number of points by the end of the season, the rules of the competition states that the top eight drivers at each Grand Prix receive 10,8,6,5,4,3,2,1 points respectively. In case of points tie, the driver with the highest number of first places leads. If still tied, then the highest second places, and so on till the highest 8th places. If still tied, then drivers are sorted lexicographically by their last and then by their first names.</p>

<p>After each race, the points received by each driver are added to his team’s pocket, and at the end of the season the team with the highest number of points wins the teams championship. To add excitement to the season, team sponsors are allowed to buy drivers from other teams even within the same season. In case of points tie between teams, teams are sorted lexicographically by their names. In this problem, you are given data of a formula one season and you’re asked to process these data according to the rules above to determine both the drivers and teams standings.</p>

### 입력 

 <p>Your program will be tested on one or more data-sets, each representing a Formula One season. All input lines are 255 characters or less. Studying the sample I/O you’ll discover that the first line of each season has an integer N, where 0 < N < 32 and representing the number of Grands Prix in that season. For each Grand Prix, the name of the Grand Prix appears on a line by itself (maximum length is 64 characters) followed by a table of the first name, last name and team name of the top eight drivers, from 1 to 8, in that Grand Prix. Each of the first and last names is a sequence of printable ASCII characters, no longer than 12 characters, and contains no spaces. Each team name is a sequence of printable ASCII characters, no longer than 18 characters, and may contain spaces (but no leading or trailing spaces.) Each team name is followed by a single period ’.’ which is not part of the name. Trailing white space may follow. A line of three -’s follows the listing of each Grand Prix. The last line of the input file contains a single zero.</p>

### 출력 

 <p>For each data set in the input you must print “Season k:” where k is the data-set number (starting from 1.) The next line must state “Drivers Standing:”. On subsequent lines list the drivers standing for that season. For each driver, print their first and last names separated by exactly one space and left justified in a field of width 25, followed by a single space, followed by the total number of points achieved by the driver during the season. The drivers standing should be followed by a blank line.</p>

<p>The next line must state “Teams Standing:” On subsequent lines list the teams standing for the that season. For each team, print the team name left justified in a field of width 25, followed by a single space, followed by the total number of points the team has scored during the season. The teams standing should be followed by a blank line.</p>

