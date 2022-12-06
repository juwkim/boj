# [Bronze IV] SMS from MCHS - 21638 

[문제 링크](https://www.acmicpc.net/problem/21638) 

### 성능 요약

메모리: 28776 KB, 시간: 68 ms

### 분류

구현(implementation)

### 문제 설명

<p>You work for MCHS (Russian Ministry of Emergency Situations). You have just received a report from Hydro-meteorological Center containing an information about today's weather and the forecast for tomorrow.</p>

<p>According to this report, the air temperature is $t_1$ degrees today, and the wind speed is $v_1$ meters per second. Tomorrow the air temperature will be $t_2$ degrees, and the wind speed will be $v_2$ meters per second.</p>

<p>You are given a task to notify citizens about the weather for tomorrow via SMS.</p>

<p>The most important goal is to warn citizens in case the storm is possible. If, according to the forecast, the temperature tomorrow will be negative, and the wind speed will be at least 10 meters per second, you should send a message with following text:</p>

<p style="text-align: center;"><code>A storm warning for tomorrow! Be careful and stay home if possible!</code></p>

<p>Otherwise, you may just notify citizens about bad weather changes.</p>

<p>If the temperature tomorrow will be lower than today, then you should send a message with a warning about a cold snap. It should have the following text:</p>

<p style="text-align: center;"><code>MCHS warns! Low temperature is expected tomorrow.</code></p>

<p>Otherwise, if wind speed tomorrow will be higher than today, then you should send a message with a warning about strong wind. It should have the following text:</p>

<p style="text-align: center;"><code>MCHS warns! Strong wind is expected tomorrow.</code></p>

<p>If none of the above conditions is satisfied, the you don't have to send a message at all.</p>

<p>Given the report from Hydro-meteorological Center, determine, what message has to be sent.</p>

### 입력 

 <p>The first line of input contains two integers $t_1$ and $v_1$ --- the temperature and the wind speed for today ($-50 \le t_1 \le 50$; $0 \le v_1 \le 20$). The second line contains two integers $t_2$ and $v_2$ --- the temperature and the wind speed for tomorrow ($-50 \le t_2 \le 50$; $0 \le v_2 \le 20$).</p>

### 출력 

 <p>In case if any message has to be sent, output its text. Otherwise, output phrase "<code>No message</code>". </p>

<p>You can separate message words with spaces and line feeds arbitrarily.</p>

