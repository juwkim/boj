# [Silver I] Legacy Code - 10856 

[문제 링크](https://www.acmicpc.net/problem/10856) 

### 성능 요약

메모리: 115124 KB, 시간: 152 ms

### 분류

그래프 이론, 그래프 탐색

### 제출 일자

2025년 5월 6일 16:24:25

### 문제 설명

<p>Once again you lost days refactoring code, which never runs in the first place. Enough is enough – your time is better spent writing a tool that finds unused code!</p>

<p>Your software is divided into packages and executables. A package is a collection of methods. Executables are packages defining among other methods exactly one method with name <code>PROGRAM</code>. This method is executed on the start of the corresponding executable. Ordinary packages have no method named <code>PROGRAM</code>.</p>

<p>Each method is uniquely identified by the combination of package and method names. E.g. the method with the identifier <code>SuperGame::PROGRAM</code> would be the main method of the executable <code>SuperGame</code>.</p>

<p>For every method in your software you are given a list of methods directly invoking it. Thus you can easily identify methods, that are never called from any method. However, your task is more challenging: you have to find unused methods. These are methods that are never reached by the control flow of any executable in your software.</p>

### 입력 

 <p>The first line of the input contains an integer N, the number of methods in your software (1 ≤ N ≤ 400).</p>

<p>Each method is described by two lines, totaling in 2·N lines. The first line consists of the unique identifier of the method and k<sub>i</sub>, the number of methods directly invoking this one (0 ≤ k<sub>i</sub> ≤ N). The second line consists of a set of ki identifiers of these calling methods or is empty if there are no such methods, i.e. k<sub>i</sub> = 0.</p>

<p>Method identifiers consist of a package name followed by two colons and a method name like <code>Packagename::Methodname</code>. Both strings, the package and the method name, each consist of up to 20 lowercase, uppercase characters or digits (a-z, A-Z, 0-9).</p>

<p>There will be exactly N different method identifiers mentioned in the input.</p>

### 출력 

 <p>A line containing the number of unused methods in your software.</p>

