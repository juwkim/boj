# [Bronze I] Hunt The Rabbit - 13777 

[문제 링크](https://www.acmicpc.net/problem/13777) 

### 성능 요약

메모리: 121220 KB, 시간: 108 ms

### 분류

이분 탐색(binary_search), 구현(implementation)

### 문제 설명

<p>Mr Farkle was brought up on a farm and spent quite a bit of time in his youth hunting rabbits! He now teaches maths and computing, and came up with a hunting game to help his students learn about the binary search.</p>

<p>He put 50 envelopes at the front of the room, numbered sequentially from 1 to 50. Inside one he hid a rabbit – not a real one, of course, just a card with a rabbit picture on it! He then put cards in all the other envelopes so that if an envelope was chosen with a number lower than the one holding the rabbit, the card would read “Try a higher number”, otherwise the card would read “Try a lower number”.</p>

<p>Students have to find the rabbit using a binary search, and write down the numbers of all the envelopes they open (in order) during their search. Remember, in a binary search you have to pick the middle envelope in the range you are searching. This is easy to find if there is an odd number of envelopes, but with an even number, you have to choose the lower numbered of the two middle envelopes. That means 25 will always be the first envelope checked.</p>

### 입력 

 <p>Each line of input will be a single number in the range 1 to 50 inclusive, it being the number of the envelope in which Mr Farkle has hidden the rabbit. The final input will be 0 which should not be processed.</p>

### 출력 

 <p>For each line of input, output the numbers of all envelopes opened, in the order they were opened, until the rabbit is found. Each number must be on the same line separated by a space from the previous number.</p>

