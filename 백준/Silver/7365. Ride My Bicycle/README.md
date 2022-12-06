# [Silver V] Ride My Bicycle - 7365 

[문제 링크](https://www.acmicpc.net/problem/7365) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

정렬(sorting)

### 문제 설명

<p>Alan Chester Mason, worried about the overuse of fossil fuels and his own expanding waist, has decided to purchase a bicycle. The model he has decided on has 3 chain rings on the crank (the gears attached to the pedal mechanism) and 7 gears on the back wheel. There is a chain connecting one front chain ring to one back gear. This selection can be changed (via the derailleurs) to any combination of front chain ring and back gear desired. The ease of pedalling is determined by the ratio of teeth in the chosen chain ring and the chosen back ring. The smaller the ratio, the easier it is to pedal. Alan has many options for the number of teeth in each chain ring and each back gear and wishes to see what the gearing (that is, ratios) would be for various combinations. You are to write a program to help him out.</p>

### 입력 

 <p>Input for this program will be the description of one configuration of chain rings and back gears. Input will be specified on two lines. The first line will have three positive integers, separated by single spaces, in strictly increasing order giving the number of teeth on each chain ring. The second line will contain 7 positive integers, separated by spaces, in strictly increasing order giving the number of teeth on each back gear. We will refer to the chain rings as chain rings 1, 2 and 3 from smallest to largest. We refer to the back gears in a similar manner.</p>

### 출력 

 <p>You should generate 21 lines of output for this program. Each line should give information about one particular combination of chain ring and back ring and should be of the form</p>

<p>x.xx f b</p>

<p>where f is the number of the chain ring, b is the number of the back ring and x.xx is the ratio of (teeth in f)/(teeth in b) given to 2 decimal places. These numbers are separated by a single space. These lines are to be printed from smallest ratio to largest. If two (or more) ratios are equal, print the one with the smallest chain ring first. You may assume that the number of teeth are such that the ratios will all be less than 10.</p>

