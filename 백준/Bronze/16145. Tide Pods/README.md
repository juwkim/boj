# [Bronze II] Tide Pods - 16145 

[문제 링크](https://www.acmicpc.net/problem/16145) 

### 성능 요약

메모리: 1120 KB, 시간: 4 ms

### 분류

구현(implementation)

### 문제 설명

<p>Many conservative commentators try to discredit the anti-gun protest movement on the grounds that we shouldn’t listen to members of a generation that eats tide pods.<sup>1</sup> The main problem with such an attack is that just because someone belongs to a group (here: American teenagers) some of whom do stupid things doesn’t mean that the individual does the same stupid things. Attacking someone based on membership in a large group typically reveals that one is not willing or able to address the actual opinion or message. Indeed, the “tide pod” argument can easily be turned around: if you are a female American teenager, you share being an American teenager with some stupid guy eating a tide pod, but you also share being female and under 21 with Malala Yousafzai. In this problem, you will compute the largest difference in opinion one could form about individuals by likening them to the best and worst other people they may resemble.</p>

<p>More precisely, you will be given a list of (binary) traits (e.g., being a teenager, being American, being female). There is a list of model people to compare an individual to: for each, you will be given which traits they possess, and a score of how “great” a person they are. The individual’s similarity to a model person is the number of traits they have in common. (Similarity is not acquired by missing the same trait: that is, we don’t say that Malala Yousafzai and Neil deGrasse Tyson have in common that they are not Swiss.) The comparison score is then the product of the number of traits they share with the score of the model person. You are to print the difference between the largest and smallest comparison score.</p>

<p><sup>1</sup>This refers to a few teenagers who posted video of themselves eating tide pods (small colorful plastic containers of laundry detergent).</p>

### 입력 

 <p>The first line contains a number K ≥ 1, which is the number of input data sets in the file. This is followed by K data sets of the following form:</p>

<p>The first line of each data set contains two integers t, n. 1 ≤ t ≤ 10 is the number of traits we use for comparing people, and 1 ≤ n ≤ 1000 is the number of model people.</p>

<p>This is followed by n lines, each describing one model person i. Each such line first contains t numbers a<sub>i,j</sub> ∈ {0, 1}, where a<sub>i,j</sub> = 1 means that person i has trait j. The last number on this line is the person’s integer score s<sub>i</sub> with −10000 ≤ s<sub>i</sub> ≤ 10000.</p>

<p>Finally, there is one line describing the individual to evaluate, containing t numbers b<sub>j</sub> ∈ {0, 1}, which capture the traits that the individual has.</p>

### 출력 

 <p>For each data set, first output “Data Set x:” on a line by itself, where x is its number. Then, output the maximum difference in scores for the individual.</p>

<p>Each data set should be followed by a blank line.</p>

