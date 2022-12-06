# [Bronze I] Stock Exchange - 6645 

[문제 링크](https://www.acmicpc.net/problem/6645) 

### 성능 요약

메모리: 31760 KB, 시간: 256 ms

### 분류

구현(implementation), 문자열(string)

### 문제 설명

<p>All stock exchanges in the world have been hit very hardly by the crisis. To keep their profit, they now try to cut down all expenses. Prague Stock Exchange would like to employ new computer software to run their operations.</p>

<p>Will you help them to develop such a system? Your task is to detect all pairs of buyers and sellers that are able to make a deal together.</p>

### 입력 

 <p>The input contains a description of several issuers.1 Each of them begins with a line containing an integer N, one space, and a code of the stock issuer. After the first one, there are N other lines, each representing one bid. A bid consists of an agent name, one space character, a word specifying the bid type in lowercase letters (either “buy” or “sell”) another space character, and a price given as a decimal number with exactly three digits after the decimal point. All buy bids always specify the maximal price, sell bids list the minimal price for which the agent wants to sell the stocks.</p>

<p>Every issuer code consist of 1–10 uppercase letters (“A”–“Z”). Agent names have at least 1 and at most 20 characters and may be composed of both lowercase and uppercase letters. For one issuer, all agent names are always unique, but the same agents may post bids for several issuers. The number of bids (N) will never exceed 1000. No price will be higher than 10 000.</p>

<p>The last line of the input contains the string “0 END”.</p>

### 출력 

 <p>For each issuer, print its code on a separate line. Then, for each agent’s bid (in the same order they were given in the input), output the name of the agent, a colon (“:”), one space, and a list of all agents that are potential counter-parties for the issuer in concern, i.e., one of them wants to buy, the other to sell and the selling price is less or equal to the buying price.</p>

<p>The agent names must be separated by a space and listed in the same order that was used in the input for that issuer. If there is no matching bid, output the string “NO-ONE” instead.</p>

