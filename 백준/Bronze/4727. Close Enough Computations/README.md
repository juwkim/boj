# [Bronze II] Close Enough Computations - 4727 

[문제 링크](https://www.acmicpc.net/problem/4727) 

### 성능 요약

메모리: 30888 KB, 시간: 128 ms

### 분류

수학(math)

### 문제 설명

<p><img alt="" src="" style="float:right; height:436px; width:222px">The nutritional food label has become ubiquitous. A sample label is shown to the right. On the label the number of calories and the number of grams of fat, carbohydrate, and protein are given as integers.</p>

<p>But carefully reading the label may cause the consumer to notice some inconsistencies. A gram of fat has 9 calories, a gram of carbohydrate has 4 calories, and a gram of protein has 4 calories. Consider the label to the right. A simple computation of the number of calories would indicate that the food should contain 12*9 + 31*4 + 5*4 or 252 calories, but the label indicates it has 250 calories.</p>

<p>While sometimes the difference in calories is due to other circumstances (such as the presence of alcohol or soluble fiber), this problem will consider only the possibility of round-off error. This food actually has 12.1 grams of fat (yielding 108.9 calories), 30.6 grams of carbohydrate (122.4 calories), 4.7 grams of protein (18.8 calories), so it does in fact have 250 calories (actually 250.1 calories).</p>

<p>Write a program that will determine if values for a nutritional label are consistent, that is, if there is a way the true values for the grams of nutrients can be rounded to the shown values and yield the number of calories shown.</p>

<p>You should assume that standard rounding rules apply; that is any value less than 0.5 rounds down and those 0.5 or over round up.</p>

### 입력 

 <p>The input will contain one or more sets of data about potential labels. Each data set will consist of 4 non-negative integers, separated by one or more blanks, on a single line. The integers represent the number of calories, the number of grams of fat, the number of grams of carbohydrates, and the number of grams of protein, in that order. The number of calories will not exceed 10000, and the number of grams of any component will not exceed 1000.</p>

<p>End of input is indicated by a line containing 4 zeroes. This line should not be processed.</p>

### 출력 

 <p>For each data set, print "yes" or "no" on its own line, indicating whether the given rounded values of the three nutrients can yield the given number of calories.</p>

