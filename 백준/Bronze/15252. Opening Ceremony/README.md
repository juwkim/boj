# [Bronze II] Opening Ceremony - 15252 

[문제 링크](https://www.acmicpc.net/problem/15252) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

구현(implementation)

### 문제 설명

<p>Olympic games always start with a beautiful opening ceremony. In addition to all kinds of dance numbers, the opening ceremony features the athletes of all participating countries walking around the main stadium, waving at the crowds, and generally acting like USC students at their graduation. And much like graduation, there are quite a few who would actually prefer to skip this ceremony, and work on their CS homeworks — sorry, we meant “train for their competitions.” That’s why each country always marches as a bloc — this way, it is easier for the organizers to tell which country has the largest number of delinquents<sup>2</sup>. Imagine how much harder this would be if the athletes were just marching in any order. You’d have to look at their jerseys and keep a careful count for each country. Well, that’s exactly what you will do!</p>

<p>You will be given for each country how many athletes it has registered. Then, you will be given a sequence of country affiliations for all athletes that marched in the opening ceremony. You are to output the maximum number of delinquents of any country.</p>

<p><sup>2</sup>And you always thought it was because each country wants to present itself as a unified group of friends?!</p>

### 입력 

 <p>The first line contains a number K ≥ 1, which is the number of input data sets in the file. This is followed by K data sets of the following form:</p>

<p>The first line of each data set contains two integers c, n. 1 ≤ c ≤ 1000 is the number of countries participating in the Olympics, and 0 ≤ n ≤ 10000 is the number of athletes at the opening ceremony.</p>

<p>This is followed by a line with c integers m<sub>1</sub>, m<sub>2</sub>, . . . , m<sub>c</sub>; here, m<sub>i</sub> ≥ 0 is the number of athletes registered for country i. Next comes a line with n integers b<sub>j</sub> ∈ {1, 2, . . . , c}. Here, b<sub>j</sub> is the country affiliation of the j th athlete in the opening ceremony. We guarantee that there will never be more than m<sub>i</sub> athletes from country i, for any i.</p>

### 출력 

 <p>For each data set, first output “Data Set x:” on a line by itself, where x is its number. Then, output the maximum number of delinquent athletes for any country.</p>

<p>Each data set should be followed by a blank line.</p>

