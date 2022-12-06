# [Bronze I] Jasio - 8417 

[문제 링크](https://www.acmicpc.net/problem/8417) 

### 성능 요약

메모리: 30840 KB, 시간: 676 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>Mały Jasio dostał bardzo trudne zadanie do rozwiązania. Ma podaną listę słów i musi policzyć ile z tych słów zawiera palindrom dłuższy niż jeden znak. Palindrom to słowo, które czytane zarówno od początku, jak i od końca, jest takie samo. Palindromem jest więc na przykład słowo ,,ala''. Natomiast słowo ,,kot'' nie jest palindromem, gdyż czytane od końca brzmi inaczej - ,,tok''. Przykładowo słowo ,,foo'' zawiera palindrom o długości większej niż jeden - jest to ciąg ,,oo'', natomiast słowo ,,ftof'' nie zawiera palindromu o długości co najmniej dwa.</p>

<p>Pojawił się pewien problem. Ponieważ Jasio nie potrafi jeszcze za dobrze czytać, nie odróżnia literki ,,i'' od literki ,,j'', a także nie rozróżnia literek ,,p'', ,,b'' oraz ,,d''. Gdy w wyrazie pojawi się literka ,,i'' lub ,,j'', Jasio traktuje je tak, jakby to był ten sam znak. To samo dotyczy ,,p'', ,,b'' i ,,d''. W związku z tym Jasio uzna za palindrom również słowo ,,pod''.</p>

<p>Potrzebny jest program, który pomoże zweryfikować rozwiązanie, które podał mały Jasio.</p>

<p>Napisz program, który:</p>

<ul>
	<li>wczyta listę słów do przetworzenia,</li>
	<li>obliczy liczbę słów na wejściu, które zawierają w sobie jakikolwiek palindrom o długości większej niż jeden znak,</li>
	<li>obliczy liczbę słów na wejściu, które Jasio uznałby za zawierające jakikolwiek palindrom o długości większej niż jeden znak,</li>
	<li>wypisze obie liczby.</li>
</ul>

### 입력 

 <p>W pierwszym wierszu znajduje się jedna liczba naturalna <i>n</i> -- liczba słów do przetworzenia, 1 ≤ <i>n</i> ≤ 10 000. Następnie znajduje się <i>n</i> wierszy, z których każdy zawiera dokładnie jedno słowo. Słowa składają się wyłącznie z małych liter alfabetu angielskiego. Długość żadnego słowa nie przekracza 200 znaków.</p>

### 출력 

 <p>Twój program powinien wypisać dokładnie dwa wiersze, każdy zawierający jedną liczbę całkowitą. Wiersz pierwszy powinien zawierać liczbę słów zawierających palindrom o długości co najmniej dwóch znaków, natomiast wiersz drugi wynik, który uzyskał mały Jasio.</p>

