# [Bronze II] Bookings - 7598 

[문제 링크](https://www.acmicpc.net/problem/7598) 

### 성능 요약

메모리: 121220 KB, 시간: 104 ms

### 분류

구현(implementation), 시뮬레이션(simulation)

### 문제 설명

<p>Air NZ (not to be confused with Air New Zealand) operate flights between various smaller cities in New Zealand. They have a number of Aerospatiale ATR72 aircraft, each with 68 seats. Their policy is that passengers must book for a particular flight, and if they fail to show up then they lose their fare. That means that, unlike other airlines, they do not have to overbook flights, so a maximum of 68 seat bookings may be made for any flight. </p>

### 입력 

 <p>In this problem you will be given one or more scenarios. Each scenario begins with a flight number and a current number of booked seats, n, (0 <= n <=68). The flight number will be the letters AZ followed by 3 digits, which will be followed by a space.</p>

<p>A number of transactions will follow, each on a single line. If the transaction is to book one or more seats, this will be presented as an upper case B followed by a space followed by an integer, n, which is the number of seats to book (0 < n <=68). Should the number of bookings requested take the number of bookings for the flight to more than 68, then that transaction must be completely ignored.</p>

<p>Customers may also cancel a booking - this will be presented as an upper case C followed by a space followed by an integer, n, which is the number of seats to cancel (0 < n <=68). Should n be greater than the number of seats currently booked, then that transaction must be completely ignored.</p>

<p>The list of transactions will be terminated by a line containing X 0 (separated by a space) which should not be processed. A line containing # 0 (separated by a space) marks the end of input. </p>

### 출력 

 <p>Output consists of one line for each flight. The line contains the flight number, followed by a space, followed by the number of seats booked for that flight after the transactions have been carried out.</p>

