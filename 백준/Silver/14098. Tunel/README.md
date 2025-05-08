# [Silver I] Tunel - 14098 

[문제 링크](https://www.acmicpc.net/problem/14098) 

### 성능 요약

메모리: 111372 KB, 시간: 108 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵, 집합과 맵

### 제출 일자

2025년 5월 8일 13:24:15

### 문제 설명

<p>Mirko stoji na ulazu, a Slavko na izlazu iz tunela. Oni zapisuju registracijske oznake automobila redom kojim oni prolaze pokraj njih i te podatke javljaju policijskoj patroli koja se nalazi nekoliko kilometara dalje.</p>

<p>Na osnovi Mirkovih i Slavkovih podataka policijska patrola može nepogrešivo utvrditi da su neki vozači pretjecali u tunelu, što je naravno strogo zabranjeno.</p>

<p>Napišite program koji će odrediti broj vozača za koje se sa sigurnošću može tvrditi da su počinili navedeni prekršaj.</p>

<p>Pretpostavljamo da je promet u tunelu protekao normalno, tj. bez sudara, bez zaustavljanja itd.</p>

### 입력 

 <p>U prvome retku nalazi se prirodan broj N (1 ≤ N ≤ 1000), broj automobila.</p>

<p>U sljedećih N redaka nalaze se registracijske oznake tih automobila, redoslijedom kojim su ulazili u tunel.</p>

<p>U sljedećih N redaka nalaze se registracijske oznake tih automobila, redoslijedom kojim su izlazili iz tunela.</p>

<p>Registracijska oznaka nekog automobila sastoji se od najmanje šest i najviše osam znakova, a jedini dozvoljeni znakovi su velika slova engleske abecede (A-Z) i znamenke dekadskog sustava (0-9). </p>

### 출력 

 <p>U prvi i jedini redak treba ispisati broj vozača koje policija sigurno može kazniti zbog nepropisnog pretjecanja.</p>

