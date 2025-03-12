# [Silver II] Shrew-ology - 4748 

[문제 링크](https://www.acmicpc.net/problem/4748) 

### 성능 요약

메모리: 112004 KB, 시간: 216 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2025년 3월 12일 23:21:11

### 문제 설명

<p>Dr. Montgomery Moreau has been observing a population of Northern Madagascar Pie-bald Shrews in the wild for many years. He has made careful observations of all the shrews in the area, noting their distinctive physical characteristics and naming each one.</p>

<p>He has made a list of significant physical characteristics (e.g., brown fur, red eyes, white feet, prominent incisor teeth, etc.) and taken note of which if these appear to be dominant (if either parent has this characteristic, their children will have it) or recessive (the children have this characteristic only if both parents have it).</p>

<p>Unfortunately, his funding from the International Zoological Institute expired and he was forced to leave the area for several months until he could obtain a new grant. During that time a new generation was born and began to mature. Upon returning, Dr. Moreau hopes to resume his work, starting by determining the likely parentage of the each member of the new generation.</p>

### 입력 

 <p>The first line of input will containing a sequence of 1 to 80 consecutive ’D’ and ’R’ characters describing a list of physical characteristics, indicating whether each is dominant or recessive.</p>

<p>After this line will follow several lines, each describing a single adult shrew. Each shrew is described by a name of 1-32 non-blank characters terminated by a blank space, then a single M or F character indicating the gender of the animal, another blank space, then a list of consecutive 0 or 1 characters, describing the animal. A 1 indicates that the animal possesses that physical characteristic, a 0 indicates that it does not. The list of adults is terminated by a line containing only the string “***”.</p>

<p>This is followed by one or more lines describing juvenile animals. These contain a name and description, each formatted identically to those for the adults, separated by a blank space. The list of juveniles is terminated by a line containing only the string “***”.</p>

### 출력 

 <p>For each juvenile animal, print a single line consisting of the animal’s name, the string “ by ”, then a (possibly empty) list of all possible parents for that animal. A set of parents should be printed as the name of the mother, a hyphen, then the name of the father. If the animal has multiple pairs of possible parents, these pairs should be printed in alphabetic (lexicographic) order first by the mother’s name, then by the father’s name among pairs where the mother is the same. Each pair should be printed separated by the string “ or ”.</p>

