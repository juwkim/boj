# [Silver IV] Coupon2 - 10184 

[문제 링크](https://www.acmicpc.net/problem/10184) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵

### 제출 일자

2023년 10월 11일 15:48:19

### 문제 설명

<p>When you go shopping and have coupons, you can only get discounts on the items you actually purchased. Before UPC codes and scanners, it was up to the cashier to check for purchases and to verify if the coupons were for valid purchases. Here is some information on UPC codes:</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/355ff6de-6eca-4199-9eae-a70a93cecc6f/-/preview/" style="width: 374px; height: 252px;"></p>

<p style="text-align: center;">(http://cdn.vouchercodes.ca/wp-content/uploads/2012/05/anatomy-of-a-upc.jpg)</p>

<p>In this program, you will have a receipt showing the UPC codes and prices. Then you will be given a list of coupons with UPC code and discount. Apply the discount to valid purchases. The UPC codes will be a 12 digit numeric sequence and the price will have no dollar sign on input.</p>

### 입력 

 <p>The first line consists of the number of data sets. The first line in each data set will consist of X and Y, the number of purchases and number of coupons. The first X lines of each data set consist of the UPC code and the price. The next Y lines consist of the UPC code and the decimal of the discount (0.20 = 20% off). X and Y will be at least 1 and at most 20, with Y <=X.</p>

### 출력 

 <p>For each data set, print out the total of the purchases. If there are invalid coupons on the purchase, print out “INVALID COUPONS” on the next line followed by the UPC codes of the invalid coupons, each on one line.</p>

