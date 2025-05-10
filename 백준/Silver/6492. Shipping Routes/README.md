# [Silver I] Shipping Routes - 6492 

[문제 링크](https://www.acmicpc.net/problem/6492) 

### 성능 요약

메모리: 108384 KB, 시간: 84 ms

### 분류

자료 구조, 플로이드–워셜, 그래프 이론, 그래프 탐색, 해시를 사용한 집합과 맵, 최단 경로, 집합과 맵

### 제출 일자

2025년 5월 11일 07:11:19

### 문제 설명

<p>The Slow Boat to China Shipping company needs a program to help them quickly quote costs to prospective customers. The cost of a shipment depends on the size of the shipment and on how many shipping legs it requires.  A shipping leg connects two warehouses, but since every pair of warehouses is not directly connected by a leg, it might require more than one leg to send a shipment from one warehouse to another.  </p>

<p>Problem Statement:   A data set can represent from 1 to 30 warehouses. A two-letter code name will identify each warehouse (capital letters only).  Shipping legs can exist between any two distinct warehouses. All legs are bidirectional. </p>

<p>The cost of a shipment is equal to the size of the shipment times the number of shipping legs required times <span>$</span>100.</p>

<p>The input to the program identifies the warehouse code names and the existence of all shipping legs.  For a given shipping request, consisting of the size of the shipment, the source warehouse and the destination warehouse, the program will output the best (cheapest) cost for the shipment, if it is possible to send shipments from the requested source to the requested destination. Alternately, the program must state that the request cannot be fulfilled. </p>

### 입력 

 <p>The first line will contain an integer from 1 to 10 inclusive that represents the number of  data sets in the input file.  Each data set represents a new shipping configuration.</p>

<p>The first line of data in a data set will contain three integers, say M, N, and P:  M is an integer from 1 to 30 inclusive representing the number of warehouses in the data set;  N is an integer from 0 to M*(M-1)/2 inclusive that represents the number of legs between warehouses in the data set; P is an integer from 0 to 10 inclusive that represents the number of shipping requests for which cost information is required.  </p>

<p>The second line of data in a data set contains M two-letter code names for the M warehouses of the data sets.  Only capital letters are used. A single blank separates code names. </p>

<p>N lines follow the line of code names, containing shipping leg information in the format: "XX  YY", with XX and YY being  the codes for two distinct warehouses in the set that have a  direct link (a shipping leg) between them. There will be a single  blank between the warehouse codes.  </p>

<p>The N lines of shipping leg information are followed by P lines of shipping requests, one request per line.  Each shipping request will begin with an integer between 1 and 20 inclusive that represents the size of the shipment.  The shipment size will be followed by a pair of code names in the format "AA  BB", with AA and BB being the code for two distinct warehouses in the set which represent the source and destination of the requested shipment.</p>

<p>The input will be valid and consistent.  A shipping leg will only be represented once within a data set.  Data about legs will always refer to warehouses that have been identified as belonging to the data set.  See the example below for clarification of the input format.</p>

### 출력 

 <p>The first line of output should read "SHIPPING ROUTES OUTPUT". For each data set there should be a section of output enumerating which data set the output section represents followed by P lines of the required information. Each of the P lines should list either the cheapest cost of the respective shipment or the phrase "NO SHIPMENT POSSIBLE". The end of the output should be noted also.  Produce output consistent with the example below.</p>

