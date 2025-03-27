# [Silver II] Hobitai - 30080 

[문제 링크](https://www.acmicpc.net/problem/30080) 

### 성능 요약

메모리: 153740 KB, 시간: 244 ms

### 분류

그리디 알고리즘, 문자열

### 제출 일자

2025년 3월 27일 10:41:20

### 문제 설명

<p><img alt="" src="https://upload.acmicpc.net/b175f3b1-e57d-4ae9-b3fc-9c617ea42f3d/-/preview/" style="width: 233px; height: 87px; float: right;">Saulėtoje kalno pusėje savo namus turi <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> hobitų. Kiekvienas hobitas gyvena vienas savo atskirame namuke. Hobitai būna arba <em>herbivorai</em> („H“), t. y. valgantys tik vaisius ir daržoves, arba <em>omnivorai</em> („O“), t. y. valgantys viską.</p>

<p>Priešpiečiams hobitai nori užsisakyti savo mėgstamų užkandžių iš maisto pristatymo traukinuko. Traukinuką sudaro <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c38"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$8$</span></mjx-container> maisto vagonėliai, galintys vienu metu atvežti maisto į aštuonis greta vienas kito esančius hobitų namukus (t. y. hobaitą). Norint užtikrinti efektyvų šio traukinuko darbą, reikia laikytis šių reikalavimų:</p>

<ul>
	<li>Užsakinėjant maistą kiekvienam iš <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c38"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$8$</span></mjx-container> vagonėlių reikia nurodyti, kokią virtuvę – herbivorų ar omnivorų – tas vagonėlis turėtų tiekti.</li>
	<li>Traukinukas važiuos palei kalną tol, kol visi vagonėliai atsidurs ties tinkamos rūšies dar neaptarnautų hobitų namukais, ir visus aštuonis namukus aptarnaus vienu metu. Tada traukinukas tęs kelionę toliau, iki kol vėl atsidurs tinkamoje padėtyje, aptarnaus kitą hobaitą, ir taip toliau. Pastaba: nors omnivorai ir yra visavalgiai, tačiau jie nesutinka valgyti herbivorams skirto maisto.</li>
	<li>Traukinukas negali apvažiuoti kalno ratu: pravažiavęs paskutinį namuką jis važiuoja ilsėtis į garažą ir toliau maistą pristatinės tik kitą dieną. Per dieną priimamas tik vienas užsakymas.</li>
</ul>

<p>Raskite, kiek daugiausiai hobitų galima pamaitinti vienu užsakymu, ir koks tas užsakymas turėtų būti.</p>

### 입력 

 <p>Pirmoje eilutėje pateiktas sveikasis skaičius <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>.</p>

<p>Antroje eilutėje pateikiama <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> simbolių eilutė. Kiekvienas jos simbolis bus arba raidė „H“, arba raidė „O“. Ši eilutė nurodo namukų išsidėstymo tvarką: „H“ raidė žymi namuką, kuriame gyvenantis hobitas yra herbivoras, o „O“ – omnivoras.</p>

### 출력 

 <p>Pirmoje eilutėje išveskite vieną sveikąjį skaičių: kiek daugiausiai hobitų gali būti aptarnauti vienu traukinuko užsakymu.</p>

<p>Antroje eilutėje išveskite tokio užsakymo pavyzdį: <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c38"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>8</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$8$</span></mjx-container> simbolius, kurių kiekvienas būtų „H“ arba „O“, nurodantys, kokio tipo užkandžius turėtų tiekti atitinkami vagonėliai. Vagonėlių išsidėstymas nurodomas tokia pačia tvarka, kokia ir hobitų namukų išsidėstymas.</p>

<p>Jei yra keli galimi atsakymo variantai, išveskite bet kurį.</p>

