# [Bronze I] 아기 석환 뚜루루 뚜루 - 15947 

[문제 링크](https://www.acmicpc.net/problem/15947) 

### 성능 요약

메모리: 29200 KB, 시간: 68 ms

### 분류

많은 조건 분기(case_work), 구현(implementation)

### 문제 설명

<p>석환이는 오늘 낮에 커피를 마셔서 잠에 들지 못하고 있다. 이불 속에서 너무 심심한 나머지 “아기 석환” 노래를 잠에 들 때까지 부르려고 한다. 석환이는 UCPC 2018 출제진 중의 한 명인 석환(seokhwan)이랑은 달리, 자신의 이름을 sukhwan이라고 쓴다. 노래가 끝나면 다시 처음부터 부른다. 아기 석환 노래는 아래와 같다.</p>

<p style="text-align: center">baby sukhwan tururu turu<br>
very cute tururu turu<br>
in bed tururu turu<br>
baby sukhwan</p>

<p>하지만 석환이는 계속 노래를 똑같이 부르기는 심심해서, 노래가 한 번 끝날 때마다 “tururu”와 “turu”에 “ru”를 한 번씩 더 추가해서 다음과 같이 부르려고 한다.</p>

<p style="text-align: center">baby sukhwan tururu turu<br>
very cute tururu turu<br>
in bed tururu turu<br>
baby sukhwan</p>

<p style="text-align: center">baby sukhwan turururu tururu<br>
very cute turururu tururu<br>
in bed turururu tururu<br>
baby sukhwan</p>

<p style="text-align: center">baby sukhwan tururururu turururu<br>
very cute tururururu turururu<br>
in bed tururururu turururu<br>
baby sukhwan</p>

<p style="text-align: center">…</p>

<p>이 때, 석환이가 부르는 노래의 N번째 단어는 무엇일까?</p>

### 입력 

 <p>첫 번째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.</p>

### 출력 

 <p>첫 번째 줄에 석환이가 N번째로 부를 단어를 출력한다. 여기서 단어란 가사 중 공백으로 구분되는 연속된 알파벳 소문자열을 뜻한다. 단, 출력할 단어가 “tururu...ru”일 때, “ru”가 k(k ≥ 5)번 반복되면 “tu+ru*k”와 같이 출력한다.</p>

