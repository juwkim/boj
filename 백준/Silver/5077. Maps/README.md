# [Silver V] Maps - 5077 

[문제 링크](https://www.acmicpc.net/problem/5077) 

### 성능 요약

메모리: 113112 KB, 시간: 108 ms

### 분류

브루트포스 알고리즘(bruteforcing), 구현(implementation)

### 문제 설명

<p>You are surveying photographic images of Antarctica for the UNADID, looking for evidence of secret (and illegal) oil drilling rigs. You are to report how many you discover.</p>

<p>You will be given a number of scenarios. Each scenario consists of an image of a secret rig and a map of a section of snowfield. Snow is represented by a dot (.) and part of a building by a X. You are to count the number of times an exact replica of the rig in the image is found on the map. “Exact” here means you do not have to count rotations or mirror images.</p>

### 입력 

 <p>The first line of input will be a single integer containing the number of scenarios.</p>

<p>Each scenario will start with one line containing two positive integers Li and Ci representing the number of lines and the number of columns in the image of the rig. Both numbers will be in the range 1 to 12 inclusive.</p>

<p>Li lines then follow, each line containing Ci characters. Each character will be an upper case X or a dot. These lines represent the image of the secret rig, which has been trimmed so there are no unnecessary snow (.) elements surrounding the rig (X) elements.</p>

<p>The next line will contain two further integers, Lm and Cm, representing the lines and columns of the map to be searched. Both numbers will be in the range 1 to 32, with Lm being no less than Li and Cm being no less than Ci.</p>

<p>Lm lines then follow, each line containing Cm characters. Each character will be an upper case X or a dot. These lines represent the map you are to search.</p>

### 출력 

 <p>Output consists of a single integer (on a line of its own) for each scenario. The integer is the number of times a secret rig was counted in the map.</p>

