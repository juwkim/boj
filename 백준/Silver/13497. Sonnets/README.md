# [Silver V] Sonnets - 13497 

[문제 링크](https://www.acmicpc.net/problem/13497) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

구현(implementation), 파싱(parsing), 문자열(string)

### 문제 설명

<p>Shakespeare wrote over 100 sonnets. You probably had to read/analyze/memorize “Shall I compare thee to a summer’s day” in school, and might have heard “Let not me to the marriage of two minds” at weddings, among others. What distinguishes a sonnet from other poems is its rhyme structure and meter. For instance, sonnets are typically in iambic pentameter, and Shakespeare’s sonnets are associated with the rhyme scheme “ABAB CDCD EFEF GG”. This means that the first line rhymes with the third, the second with the fourth, the fifth with the seventh, etc. We will ignore the meter for this problem, and just focus on the rhyme scheme.</p>

<p>You will be given poems to analyze. To save you a lot of work, we will already give you the syllable and stress structure: syllables will be separated by hyphens (which will not be used otherwise), and stressed syllables will be in all-caps, while others will be all lowercase (even if this means starting a sentence with a lowercase letter). Since pronunciation of English is not easy to infer from the writing, we simplify rhyming as follows. In each line, we look at the last stressed syllable and all (0 or more) subsequent unstressed syllables. Then look at the sequence of all vowels (‘a’, ‘e’, ‘i’, ‘o’, ‘u’, ‘y’) in those syllables combined. Two lines rhyme if that sequence is the exact same for both of them. The first line will be denoted by A, as will all lines that rhyme with it. The first line that doesn’t rhyme with it will be B, as will all lines rhyming with it, and so on. An empty line translates to a space in the rhyme scheme.</p>

### 입력 

 <p>The first line is the number K of input data sets, followed by K data sets, each of the following form:</p>

<p>The first line contains an integers 1 ≤ n ≤ 26, the number of lines in the poem. This is followed by n lines of text, consisting of upper- and lowercase letters (as discussed above), hyphens (separating syllables), spaces (separating words, and thus also syllables), and the punctuation marks ‘.’, ‘,’, ‘:’, ‘;’, which also separate words. Each syllable will be at most 6 characters long, and each line at most 100 characters. Each non-empty line will have at least one stressed syllable.</p>

### 출력 

 <p>For each data set, output “Data Set x:” on a line by itself, where x is its number. Then, on a line by itself, output the rhyme scheme.</p>

<p>Each data set should be followed by a blank line.</p>

