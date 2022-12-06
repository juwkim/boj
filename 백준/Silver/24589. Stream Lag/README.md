# [Silver V] Stream Lag - 24589 

[문제 링크](https://www.acmicpc.net/problem/24589) 

### 성능 요약

메모리: 114328 KB, 시간: 160 ms

### 분류

구현(implementation)

### 문제 설명

<p>Live stream audiences often encounter undesired stream lag. The lag may occur for multiple reasons, such as slow network speed, high stream resolution, not enough processing power on the client hardware, etc. In this problem, we will model and compute the stream lag for one hypothetical stream.</p>

<p>The stream has a video content that is segmented into n network packets to send, numbered from 1 to n. Each packet contains a small segment of the streamed video with a length of exactly one second. A stream lag is a time period in which the stream audience is not watching any content while waiting for the stream packets to arrive. Ideally, a stream audience experiencing zero lag shall receive packet i at the beginning of the ith second, in which case the audience can seamlessly watch the entire streamed video.</p>

<p>In reality, any of the n packets may be received at any moment, and not necessarily in order from 1 to n. A stream client will only start playing packet i if it has played all its preceding packets. If this is not the case, the stream client will wait until all packets before i have been received and played. The stream client keeps all received packets that cannot yet be played in its buffer and is able to retrieve them in no time when they are ready to be played. If a packet is not available when the time to play it arrives, the stream lags and viewers fall behind from the live stream. The stream client plays each packet for exactly one second at its original speed. All packets are to be played even when the play time lags much behind the live stream.</p>

<p>Given the arrival time of the n packets in chronological order, compute the total lag time that a stream audience will experience.</p>

### 입력 

 <p>The first line of input has a single integer n (1 ≤ n ≤ 1,000). This is followed by n lines. The ith line has two integers t<sub>i</sub> and i (1 ≤ t<sub>i</sub> ≤ 10<sup>9</sup>, 1 ≤ i ≤ n), which means that packet i arrives at the beginning of the t<sub>i</sub> th second. The values of t<sub>i</sub>’s are non-decreasing. Packets may arrive at the same time.</p>

### 출력 

 <p>Output the total lag time based on the given packet arrival time.</p>

