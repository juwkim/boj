# [Silver V] Humidex - 4238 

[문제 링크](https://www.acmicpc.net/problem/4238) 

### 성능 요약

메모리: 32952 KB, 시간: 72 ms

### 분류

구현(implementation), 수학(math)

### 문제 설명

<p><strong>Adapted from Wikipedia, the free encyclopedia</strong></p>

<p>The humidex is a measurement used by Canadian meteorologists to reflect the combined effect of heat and humidity. It differs from the heat index used in the United States in using dew point rather than relative humidity.</p>

<p>When the temperature is 30 C (86 F) and the dew point is 15 C (59 F), the humidex is 34 (note that humidex is a dimensionless number, but that the number indicates an approximate temperature in C). If the temperature remains 30 C and the dew point rises to 25 C (77 F), the humidex rises to 42.3.</p>

<p>The humidex tends to be higher than the U.S. heat index at equal temperature and relative humidity.</p>

<p>The current formula for determining the humidex was developed by J.M. Masterton and F.A. Richardson of Canada's Atmospheric Environment Service in 1979.</p>

<p>According to the Meteorological Service of Canada, a humidex of at least 40 causes "great discomfort" and above 45 is "dangerous." When the humidex hits 54, heat stroke is imminent.</p>

<p>The record humidex in Canada occurred on June 20, 1953, when Windsor, Ontario hit 52.1. (The residents of Windsor would not have known this at the time, since the humidex had yet to be invented.) More recently, the humidex reached 50 on July 14, 1995 in both Windsor and Toronto.</p>

<p>The humidex formula is as follows:</p>

<pre>    humidex = temperature + h
    h = (0.5555)*(e - 10.0)
    e = 6.11 * exp [5417.7530 * ((1/273.16) - (1/(dewpoint+273.16)))]
</pre>

<p>where exp(x) is 2.718281828 raised to the exponent x.</p>

<p>While humidex is just a number, radio announcers often announce it as if it were the temperature, e.g. "It's 47 degrees out there ... [pause] .. with the humidex,". Sometimes weather reports give the temperature and dewpoint, or the temperature and humidex, but rarely do they report all three measurements. Write a program that, given any two of the measurements, will calculate the third.</p>

<p>You may assume that for all inputs, the temperature, dewpoint, and humidex are all between -100 C and 100 C.</p>

### 입력 

 <p>Input will consist of a number of lines. Each line except the last will consist of four items separated by spaces: a letter, a number, a second letter, and a second number. Each letter specifies the meaning of the number that follows it, and will be either T, indicating temperature, D, indicating dewpoint, or H, indicating humidex. The last line of input will consist of the single letter E.</p>

### 출력 

 <p>For each line of input except the last, produce one line of output. Each line of output should have the form:</p>

<pre>T number D number H number</pre>

<p>where the three numbers are replaced with the temperature, dewpoint, and humidex. Each value should be expressed rounded to the nearest tenth of a degree, with exactly one digit after the decimal point. All temperatures are in degrees celsius.</p>

