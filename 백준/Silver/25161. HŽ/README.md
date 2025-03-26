# [Silver II] HŽ - 25161 

[문제 링크](https://www.acmicpc.net/problem/25161) 

### 성능 요약

메모리: 110760 KB, 시간: 108 ms

### 분류

브루트포스 알고리즘, 구현, 정렬

### 제출 일자

2025년 3월 27일 06:26:14

### 문제 설명

<p>Na jednoj pruzi postoji N željezničkih postaja označenih brojevima od jedan do N. Zbog obnove, K dijelova pruge je zatvoreno, na njima se ne može prometovati niti u jednom smjeru te se na tim dijelovima putnici prevoze autobusima. Dijelovi pruge koji su zatvoreni zadani su svojim početnim i završnim postajama.</p>

<p>Zamislimo sada jednu situaciju. Putnik dođe na postaju X te kupi kartu za putovanje do postaje Y. Ako se na putu između postaja X i Y putnici u nekom trenutku prevoze autobusima, to treba obavezno pisati na kupljenoj karti. Zamislimo da proučavamo M takvih situacija.</p>

<p>Odgovori na sljedeća pitanja:</p>

<ol>
	<li>Na koliko je, od M kupljenih karti, pisalo da se dio ili cijeli put putnici prevoze autobusima?</li>
	<li>Koliko najmanje od K dijelova treba otvoriti da na niti jednoj od M karti ne piše upozorenje?</li>
	<li>Koliki je najdulji dio pruge, izražen u broju postaja, na kojem se možemo voziti samo vlakom?</li>
</ol>

### 입력 

 <p>U prvom je retku prirodan broj N (1 ≤ N ≤ 1000), broj iz teksta zadatka.</p>

<p>U drugom je retku prirodan broj K (1 ≤ K ≤ 1000), broj iz teksta zadatka.</p>

<p>U sljedećih K redaka nalaze se po dva prirodna broja P<sub>i</sub> (1 ≤ P<sub>i</sub> ≤ N) i K<sub>i</sub> (1 ≤ K<sub>i</sub> ≤ N, P<sub>i</sub> ≠ K<sub>i</sub>), oznake početne i završne postaje na i-tom zatvorenom dijelu pruge. Zadani zatvoreni dijelovi se ne sijeku.</p>

<p>U sljedećem je retku prirodan broj M (1 ≤ M ≤ 1000), broj iz teksta zadatka.</p>

<p>U sljedećih M redaka nalaze se po dva prirodna broja X<sub>i</sub> (1 ≤ X<sub>i</sub> ≤ N) i Y<sub>i</sub> (1 ≤ Y<sub>i</sub> ≤ N, X<sub>i</sub> ≠ Y<sub>i</sub>), oznake postaja iz teksta zadatka za i-tu promatranu situaciju.</p>

### 출력 

 <p>U prvi redak ispiši cijeli broj, odgovor na prvo pitanje iz teksta zadatka.</p>

<p>U drugi redak ispiši cijeli broj, odgovor na drugo pitanje iz teksta zadatka.</p>

<p>U treći redak ispiši cijeli broj, odgovor na treće pitanje iz teksta zadatka.</p>

