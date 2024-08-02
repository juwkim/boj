# [Bronze I] Basket - 26360 

[문제 링크](https://www.acmicpc.net/problem/26360) 

### 성능 요약

메모리: 108080 KB, 시간: 116 ms

### 분류

구현, 수학

### 제출 일자

2024년 8월 2일 17:57:27

### 문제 설명

<p>Perica programira simulaciju koju će košarkaški suci koristiti za online učenje pravila košarkaške igre. Jedna od situacija koja se pojavljuje tijekom igre opisana je na sljedeći način:</p>

<ul>
	<li>igrač ekipe koja je u napadu šutira, tj. baca loptu prema košu. Ako igrač pogodi koš, sudac njegovoj ekipi dodjeljuje X poena. Ako igrač ne pogodi, ekipa ne dobija poene za taj šut.</li>
	<li>dodatno, igrač u trenutku upućivanja lopte prema košu može biti nepropisno zaustavljen od strane protivničkog igrača. Ako se to dogodi, sudac prvo sačeka hoće li igrač pogoditi koš i onda donese dodatnu odluku:
	<ul>
		<li>igrač je pogodio koš - sudac igraču dodjeljuje još jedno dodatno bacanje u koš;</li>
		<li>igrač nije pogodio koš - sudac igraču dodijeljuje još X dodatnih bacanja.</li>
	</ul>
	</li>
</ul>

<p>Igrač svako dodatno bacanje može pogoditi ili promašiti. Za svako pogođeno bacanje sudac ekipi dodjeljuje jedan poen.</p>

<p>Za testiranje simulacije, Perica je pripremio jednu probnu situaciju. Napiši program koji će ispisati koliko je poena imala ekipa nakon odigrane situacije.</p>

### 입력 

 <p>U prvom je retku prirodan broj X (2 ≤ X ≤ 10), broj iz teksta zadatka.</p>

<p>U drugom je retku cijeli broj 0 ili 1. Nula – igrač je promašio; jedan – igrač je pogodio šut za X poena.</p>

<p>U trećem je retku cijeli broj 0 ili 1. Jedan – igrač je prilikom izvođenja šuta za X poena nepropisno zaustavljen; nula – igrač nije nepropisno zaustavljen.</p>

<p>Ovisno o vrijednostima u drugom i trećem retku slijedi nula, jedan ili X redaka nula ili jedinica. Jedinica označava da je igrač pogodio dodatno bacanje, a nula da igrač nije pogodio dodatno bacanje.</p>

### 출력 

 <p>U jedini redak ispiši broj poena iz teksta zadatka.</p>

