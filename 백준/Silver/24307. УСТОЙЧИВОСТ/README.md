# [Silver I] УСТОЙЧИВОСТ - 24307 

[문제 링크](https://www.acmicpc.net/problem/24307) 

### 성능 요약

메모리: 108384 KB, 시간: 92 ms

### 분류

수학, 런타임 전의 전처리

### 제출 일자

2025년 1월 2일 19:58:03

### 문제 설명

<p>Както може би знаете от предни задачи, когато скучае, Ели взима някакво неотрицателно цяло число, разбива го на цифри, умножава цифрите и получава ново такова число. Например, избирайки 42, тя получава 8, избирайки 666 тя получава 216, и избирайки 1337 тя получава 63.</p>

<p>Момичето забеляза, че може да направи същото върху резултата от числото, което е избрала, Например, започвайки с 1337, тя получава 63, на което също може да умножи цифрите, получавайки 6 * 3 = 18. Тя може да продължи дори още, получавайки 1 * 8 = 8. Когато стигне до едноцифрено число, момичето спира, тъй като няма какво повече да направи.</p>

<p>Ели нарича „устойчивост“ на числото броя на итерациите за прилагане на горната процедура, необходими за да се достигне до едноцифрено число. Например, устойчивостта на 3 е нула (то вече е едноцифрено), устойчивостта на 42 е 1 (след една итерация то става 8), а устойчивостта на 666 и 1337 е 3 (666 ⇒ 216 ⇒ 12 ⇒ 2 и 1337 ⇒ 63 ⇒ 18 ⇒ 8).</p>

<p>Изведнъж Ели се зачуди кое е най-малкото число с дадена устойчивост? Например, макар и 666 и 1337 да имат устойчивост 3, най-малкото число с тази устойчивост всъщност е едва 39 (39 ⇒ 27 ⇒ 14 ⇒ 4). Сега момичето ви моли да намерите най-малкото число, имащо дадена устойчивост P.</p>

### 입력 

 <p>На единствен ред на стандартния вход ще бъде зададено едно цяло число P – устойчивостта, която интересува Ели.</p>

### 출력 

 <p>На единствен ред на стандартния изход изведете едно неотрицателно цяло число – минималното, което има устойчивост P.</p>

