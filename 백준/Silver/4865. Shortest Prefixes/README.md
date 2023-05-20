# [Silver IV] Shortest Prefixes - 4865 

[문제 링크](https://www.acmicpc.net/problem/4865) 

### 성능 요약

메모리: 115616 KB, 시간: 184 ms

### 분류

브루트포스 알고리즘, 문자열

### 문제 설명

<p>A prefix of a string is a substring starting at the beginning of the given string. The prefixes of "carbon" are: "c", "ca", "car", "carb", "carbo", and "carbon". Note that the empty string is not considered a prefix in this problem, but every non-empty string is considered to be a prefix of itself. In everyday language, we tend to abbreviate words by prefixes. For example, "carbohydrate" is commonly abbreviated by "carb". In this problem, given a set of words, you will find for each word the shortest prefix that uniquely identifies the word it represents.</p>

<p>In the sample input below, "carbohydrate" can be abbreviated to "carboh", but it cannot be abbreviated to "carbo" (or anything shorter) because there are other words in the list that begin with "carbo".</p>

<p>An exact match will override a prefix match. For example, the prefix "car" matches the given word "car" exactly. Therefore, it is understood without ambiguity that "car" is an abbreviation for "car" , not for "carriage" or any of the other words in the list that begins with "car".</p>

### 입력 

 <p>The input file contains at least two, but no more than 1000 lines. Each line contains one word consisting of 1 to 20 lower case letters. The words are unique, so you cannot have "ab" twice in the input.</p>

### 출력 

 <p>The output file contains the same number of lines as the input file. Each line of the output file contains the word from the corresponding line of the input file, followed by one blank space, and the shortest prefix that uniquely (without ambiguity) identifies this word.</p>

