# [Bronze I] Bukmacherzy - 8827 

[문제 링크](https://www.acmicpc.net/problem/8827) 

### 성능 요약

메모리: 30840 KB, 시간: 72 ms

### 분류

사칙연산(arithmetic), 브루트포스 알고리즘(bruteforcing), 구현(implementation), 수학(math)

### 문제 설명

<p>Tata Hektora zainteresował się ostatnio zakładami sportowymi. Wktórce ma odbyć się mecz w bierki podwodne pomiędzy drużynami Alfa i Beta.</p>

<p>Pobliski bukmacher wypłaci X zł za każdą złotówkę postawioną na zwycięstwo drużyny Alfa, jeśli ta drużyna wygra mecz. Analogicznie, jeśli spotkanie wygra dużyna Beta, bukmacher wypłaci Y zł za każdą złotówkę postawioną na taki rezultat ( w bierki podwodne oczywiście nie da się zremisować).</p>

<p>Tata Hektora nie chce ryzykować pechowej utraty pieniędzy. Chciałby dowiedzieć się, czy da się tak dobrać kwotę A stawianą na zwycięstwo zespołu Alfa i kwotę B stawianą na zwycięstwo zespołu Beta, aby niezależnie od wyniku meczu otrzymać nagrodę większą od A+B.</p>

<p>Czy potrafisz napisać program, który odpowie na to pytanie?</p>

### 입력 

 <p>W pierwszej linii wejścia znajduje się liczba zestawów testowych Z ( 1 <= Z <= 10 ).</p>

<p>W każdej z kolejnych Z linii znajdują się 2 liczby rzeczywiste X (1<X<=1000)  i Y (1<Y<=1000), każda będzie podana z dwoma miejscami po przecinku.</p>

### 출력 

 <p>Dla każdego przypadku testowego wypisz w osobnej linii:</p>

<ul>
	<li>"TAK" gdy da się obstawić pieniądze sposób gwarantujący zysk</li>
	<li>"NIE" w przeciwnym wypadku</li>
</ul>

