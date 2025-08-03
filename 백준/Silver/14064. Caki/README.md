# [Silver I] Caki - 14064 

[문제 링크](https://www.acmicpc.net/problem/14064) 

### 성능 요약

메모리: 110868 KB, 시간: 92 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2025년 8월 4일 04:50:29

### 문제 설명

<p>Mali Caki obožava utrke bolida Formule 1, a nova sezona upravo je počela. Prošle je nedjelje Caki sjeo ispred štale, izvukao antenu na svom radiju, usmjerio je u obližnji repetitor i pomno slušao prijenos utrke. I sve bi bilo krasno da se komentator utrke nije odlučio našaliti sa svojim slušateljima tako da je na početku prijenosa najavio da će jedine informacije koje će prenositi u eter biti oznaka bolida koji prestiže bolid ispred sebe i to upravo u trenutku prestizanja. Staza na kojoj se utrka odvija je kružna, a pretpostavljamo da su svi bolidi stigli na cilj nakon što su odvozili propisani broj krugova.</p>

<p>Iz dobivenih informacije odredite koji su bolidi zauzeli prvih šest mjesta na kraju utrke. Primijetite da je moguće da bolid prestigne druge bolide za cijeli krug ili više krugova.</p>

### 입력 

 <p>U prvom redu nalaze se dva prirodna broja n i k, (2 ≤ n ≤ 1 000, 1 ≤ k ≤ 10 000) — broj bolida na stazi te broj prestizanja tijekom utrke. Bolidi su označeni brojevima od 1 do n, i to tako da je svaki bolid označen upravo onim brojem koji predstavlja njegovu startnu poziciju.</p>

<p>U svakom od sljedećih k redaka nalazi se po jedan prirodni broj x (1 ≤ x ≤ n) — oznaka bolida koji je prestigao bolid ispred sebe. Tih k brojeva poredani su upravo onim redoslijedom kako su se prestizanja i dogadala.</p>

### 출력 

 <p>U prvi red ispišite oznake bolida koji su zauzeli prvih šest mjesta na kraju utrke. Prvi broj je oznaka bolida koji je zauzeo prvo mjesto, . . . , šesti broj je oznaka bolida koji je zauzeo šesto mjesto, a ti su brojevi odvojeni s po jednim razmakom. Ako je broj bolida manji od šest, potrebno je ispisati točno onoliko brojeva koliko je bolida sudjelovalo u utrci.</p>

