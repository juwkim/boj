# [Silver II] Monkeys at Typewriters - 5166 

[문제 링크](https://www.acmicpc.net/problem/5166) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

수학, 문자열

### 제출 일자

2025년 3월 13일 22:56:00

### 문제 설명

<p>You’ve probably all heard at some point that if you were to sit down enough monkeys at typewriters, and let them type for long enough, they would eventually type all of Shakespeare’s works. The assumption is that the monkeys will hit a completely random sequence of keys. It’s usually not clear what point people are trying to make when they bring the “monkeys at typewriters” up; sometimes, it is about the fact that randomness contains structure, or that there isn’t really that much artistic about writing poetry and plays. People who are skilled at math instead use it to argue just how extremely unlikely it is that the monkeys would produce anything meaningful, or just how many monkeys, typewriters, and how much time one would need.</p>

<p>Here, we’ll solve a related question: given a collection of words, and monkeys typing randomly until they hit the space bar for the first time, what’s the probability that they’ll accidentally write one of the given words? All words will consist only of lowercase letters. You will be given the probabilities of hitting each of the lowercase letters, as well as that of hitting the space bar. Those probabilities will sum up to 1. The assumption is that the monkeys will keep hitting random keys according to this distribution until they hit the space bar, and then stop typing. You will also be given the list of words, and your goal is to compute the probability of the monkey typing one of the given words. A monkey is considered as having typed a word if the sequence up to the space bar matches that word exactly.</p>

### 입력 

 <p>The first line contains the number K of data sets. This is followed by K data sets, each of the following form:</p>

<p>The first line contains three numbers n, m, s (1 ≤ n ≤ 100, 1 ≤ m ≤ 26, 0 ≤ s ≤ 1). n is the number of words we want the monkeys to produce, m is the number of letter keys on the typewriter, and s is the probability of hitting the space bar. This is followed by m lines, each containing a letter and a floating point number, specifying the probability of the monkey hitting that letter. The probabilities, including the space bar probability, will add up to 1. Finally, there will be n lines, each containing a word wi. Each word wi consists only of lower-case letters which are also available on the typewriter, and has between 1 and 20 characters. All the words will be distinct.</p>

### 출력 

 <p>For each data set, output “Data Set x:” on a line by itself, where x is its number. Then, on the next line, output the probability of typing at least one of the given words. Since these probabilities can be very small, you should output them using scientific notation with four decimals after the dot, e.g., 3.7602E − 13. See the front page of this problem set for a hint on how to do that. Each data set should be followed by an empty line.</p>

