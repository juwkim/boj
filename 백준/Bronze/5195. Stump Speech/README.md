# [Bronze I] Stump Speech - 5195 

[문제 링크](https://www.acmicpc.net/problem/5195) 

### 성능 요약

메모리: 30840 KB, 시간: 1300 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>It used to be that a candidate would simply state to potential voter what he thought, and what (s)he was going to do and vote for<sup>3</sup>. Nowadays, each statement and speech is carefully prepared and focus-group tested, to make sure that it does not elicit any negative reactions, or create any unwanted associations. Focus groups are literally sat down with levers in their hands, and while listening to the speech, are asked to trace with the lever how positive they feel about the candidate. Based on the feedback, the speech is then altered.</p>

<p>Wouldn’t it be much easier if we could save ourselves the trouble of getting an actual focus group, and instead had a computer program that would tell us how people would react to a speech? Here, we are going to write a program that gives a first rudimentary approximation to this functionality. You will be given a list of key words and phrases, and the reactions they elicit. Based on those, you are to assess the quality of the speech.</p>

<p>More specifically, each phrase has a positive or negative score attached with it, for instance, “taxes” could have a score of -2, “increase taxes” a score of -4, “education” a score of 3, and “slash education” a score of -6. You would then count the number of times each of these phrases occurs in the text, and add the corresponding scores, to obtain the score of the speech.</p>

<p><sup>3</sup>perhaps fibbing a little — even the good old times were not that good.</p>

### 입력 

 <p>The first line contains a number K ≥ 1, which is the number of input data sets in the file. This is followed by K data sets of the following form:</p>

<p>The first line of each data set contains a number n, the number of words or phrases eliciting emotions.</p>

<p>This is followed by n pairs of lines. The first line of each pair contains a key phrase of at most 80 characters, consisting entirely of lower-case letters and white space. The second line of each pair contains the score, a positive or negative integer.</p>

<p>This is followed by one more line of at most 10000 characters, containing the candidate’ speech. This string consists only of lowercase letters, white space, and the punctuation signs ‘.’ and ‘,’. (In the example below, there are line breaks, in order to display the input properly. There won’t be any line breaks as part of the text in the actual test files.)</p>

### 출력 

 <p>For each data set, first output “Data Set x:” on a line by itself, where x is its number. Then, output the score of the proposed text on a line by itself. The score is the sum over all key phrases that occur in the text (if they occur multiple times, they are scored multiple times). Only exact matches count — if as much as the amount of white space is different, we assume that it is not the key phrase.</p>

