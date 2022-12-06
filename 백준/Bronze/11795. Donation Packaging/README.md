# [Bronze III] Donation Packaging - 11795 

[문제 링크](https://www.acmicpc.net/problem/11795) 

### 성능 요약

메모리: 121220 KB, 시간: 128 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>ICPC donation center is preparing donation packages for people who faced disaster in every area in Thailand. The center gets several kinds of donation. In this year, the center gets a request to pack the basic items in one package which consists of three sets. The first set, called SetA, is water and beverage. The second one, SetB, consists of instant noodle, canned food and rice. And the last set, SetC, is first aid kits and tissue paper. In every day, we try to pack and distribute donation packages as many as possible. We have constrains for packaging which are: one package has to comprise of SetA , SetB and SetC equally and one distribution contains the minimum of 30 packages. However, the center receives these 3 sets in different amount each day. Therefore, the center must wait until the accumulated amount of each and every set over 30 in order to pack a distribution.</p>

### 입력 

 <p>The input will start with an integer T (1<= T <= 365), the number of consecutive donation days. The next T lines show donation in each day, consisting of three integers: the number of setA, SetB and setC, respectively.</p>

### 출력 

 <p>For each day, print out the maximum number of packages to be distributed on that day. If the packages cannot be distributed on that day (number of packages is less than 30), print NO. </p>

