# [Silver V] Eurokulen - 25449 

[문제 링크](https://www.acmicpc.net/problem/25449) 

### 성능 요약

메모리: 141636 KB, 시간: 508 ms

### 분류

구현(implementation), 정렬(sorting)

### 문제 설명

<p>Na izboru za najbolji kulen Europe sudjeluje $N$ malih obiteljskih gospodarstava (OPG) označenih brojevima od jedan do $N$. Nakon predstavljanja i degustacije kulena, pristupa se glasanju. Svaki OPG-e rangira preostalih $N-1$ OPG-ova na način da najboljem kulenu po njihovom izboru dodijeli N-1 bodova, donajboljem $N-2$ bodova i tako sve do zadnjeg kojem dodjeljuje samo jedan bod.</p>

<p><strong>Pitanje #1</strong>: Odredi i ispiši oznake OPG-ova čiji su kuleni zauzeli prvo, drugo i treće mjesto. Ako više kulena ima isti broj bodova, prednost ima onaj s manjom oznakom.</p>

<p>Međutim, europski povjerenik za kulen, izvjesni K.M. iz Zagreba, dodatno pregledava ishod glasanja. Naime, Europa ne voli kada OPG-ovi razmjenjuju bodove, tj. kada OPG A da X bodova OPG-u B, a OPG B da X bodova OPG-u A. Kada povjerenik otkrije takvu situaciju, glasovi OPG-a A i OPG-a B se brišu i ne broje se u određivanju nove liste najboljih kulena. Njihovi kuleni ostaju na listi, samo se njihovi glasovi brišu.</p>

<p><strong>Pitanje #2</strong>: Odredi i ispiši oznake OPG-ova čiji su kuleni zauzeli prvo, drugo i treće mjesto nakon brisanja bodova OPG-ova koji su razmjenjivali bodove. Ako više kulena ima isti broj bodova, prednost ima onaj s manjom oznakom.</p>

### 입력 

 <p>U prvom je retku prirodan broj $N$ ($3 ≤ N ≤ 1000$), broj iz teksta zadatka.</p>

<p>U $i$-tom od sljedećih $N$ redaka je $N-1$ prirodnih brojeva $K_j$ ($1 ≤ K_j ≤ N-1$, $K_j ≠ i$), oznake kulena onim redom kako ih je OPG oznake $i$ rangirao.</p>

### 출력 

 <p>U prvi redak ispiši tražene tri oznake OPG-ova, odgovor na prvo pitanje iz teksta zadatka.</p>

<p>U drugi redak ispiši tražene tri oznake OPG-ova, odgovor na drugo pitanje iz teksta zadatka.</p>

