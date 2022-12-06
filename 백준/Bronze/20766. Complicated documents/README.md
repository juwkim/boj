# [Bronze I] Complicated documents - 20766 

[문제 링크](https://www.acmicpc.net/problem/20766) 

### 성능 요약

메모리: 30996 KB, 시간: 1012 ms

### 분류

구현(implementation), 파싱(parsing), 문자열(string)

### 문제 설명

<p>Roman is a tech writer in a big IT company, Textawei. His work consists in writing technical documentations, rules, specifications, etc. The volumes of the texts he has written are immense. Everything was going great until one day he received a letter from his boss... The letter stressed the importance of keeping the information in the documents relevant and keep the style consistent, and there was an attachment with a set of rules --- the description of the style. Moreover, they set up a whole system to check all text files and point out inconsistencies. </p>

<p>Roman rushed to view the report on his documents and saw around 100500 urgent problems. Despite his massive grief, Roman bravely decided to analyze his mistakes. It turned out that the majority of the inconsistencies had to do with a single rule, which stated: "Before and after each colon and dash there must be at least one space or beginning/end of line".</p>

<p>At this point, Roman realized that he could come up with a program to fix his documents, at least in regards to this particular rule. The program would add the minimal number of spaces to the text in such a way that the rule is satisfied.</p>

<p>Unfortunately, Roman is a tech writer and cannot code. Help him!</p>

### 입력 

 <p>The first line of the input file contains a single integer $T$ --- the number of lines in the text ($1 \le T \le 10\,000$). Next come $T$ lines --- the document text.</p>

<p>It is guaranteed that the total number of characters in the text is not greater than $10\,000$. All characters have ASCII-codes from 32 to 126 inclusive.</p>

### 출력 

 <p>Print the corrected text into the output file.</p>

