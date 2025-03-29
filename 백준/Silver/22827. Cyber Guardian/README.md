# [Silver II] Cyber Guardian - 22827 

[문제 링크](https://www.acmicpc.net/problem/22827) 

### 성능 요약

메모리: 114156 KB, 시간: 264 ms

### 분류

구현, 파싱, 문자열

### 제출 일자

2025년 3월 30일 04:08:20

### 문제 설명

<p>In the good old days, the Internet was free from fears and terrorism. People did not have to worry about any cyber criminals or mad computer scientists. Today, however, you are facing atrocious crackers wherever you are, unless being disconnected. You have to protect yourselves against their attacks.</p>

<p>Counting upon your excellent talent for software construction and strong sense of justice, you are invited to work as a cyber guardian. Your ultimate mission is to create a perfect firewall system that can completely shut out any intruders invading networks and protect children from harmful information exposed on the Net. However, it is extremely difficult and none have ever achieved it before. As the first step, instead, you are now requested to write a software simulator under much simpler assumptions.</p>

<p>In general, a firewall system works at the entrance of a local network of an organization (e.g., a company or a university) and enforces its local administrative policy. It receives both inbound and outbound packets (note: data transmitted on the Net are divided into small segments called packets) and carefully inspects them one by one whether or not each of them is legal. The definition of the legality may vary from site to site or depend upon the local administrative policy of an organization. Your simulator should accept data representing not only received packets but also the local administrative policy.</p>

<p>For simplicity in this problem we assume that each network packet consists of three fields: its source address, destination address, and message body. The source address specifies the computer or appliance that transmits the packet and the destination address specifies the computer or appliance to which the packet is transmitted. An address in your simulator is represented as eight digits such as 03214567 or 31415926, instead of using the standard notation of IP addresses such as 192.168.1.1. Administrative policy is described in filtering rules, each of which specifies some collection of source-destination address pairs and defines those packets with the specified address pairs either legal or illegal.</p>

### 입력 

 <p>The input consists of several data sets, each of which represents filtering rules and received packets in the following format:</p>

<pre>n m
rule1
rule2
...
<i>rule<sub>n</sub></i>
<i>packet</i><sub>1</sub>
<i>packet</i><sub>2</sub>
...
<i>packet</i><sub>m</sub></pre>

<p>The first line consists of two non-negative integers <i>n</i> and <i>m</i>. If both <i>n</i> and <i>m</i> are zeros, this means the end of input. Otherwise, <i>n</i> lines, each representing a filtering rule, and <i>m</i> lines, each representing an arriving packet, follow in this order. You may assume that <i>n</i> and <i>m</i> are less than or equal to 1,024.</p>

<p>Each <i>rule<sub>i</sub></i> is in one of the following formats:</p>

<dir>
</dir>

<ul>
	<li>permit <i>source-pattern</i> <i>destination-pattern</i></li>
	<li>deny <i>source-pattern</i> <i>destination-pattern</i></li>
</ul>

<p>A <i>source-pattern</i> or <i>destination-pattern</i> is a character string of length eight, where each character is either a digit ('0' to '9') or a wildcard character '?'. For instance, "1????5??" matches any address whose first and fifth digits are '1' and '5', respectively. In general, a wildcard character matches any single digit while a digit matches only itself.</p>

<p>With the keywords "permit" and "deny", filtering rules specify legal and illegal packets, respectively. That is, if the source and destination addresses of a packed are matched with <i>source-pattern</i> and <i>destination-pattern</i>, respectively, it is <i>permitted</i> to pass the firewall or the request is <i>denied</i> according to the keyword. Note that a permit rule and a deny rule can contradict since they may share the same source and destination address pair. For the purpose of conflict resolution, we define a priority rule: <i>rule<sub>i</sub></i> has a higher priority over <i>rule<sub>j</sub></i> if and only if <i>i</i> > <i>j</i>. For completeness, we define the default rule: any packet is illegal unless being explicitly specified legal by some given rule.</p>

<p>A packet is in the following format:</p>

<dir>
</dir>

<ul>
	<li><i>source-address</i> <i>destination-address</i> <i>message-body</i></li>
</ul>

<p>Each of the first two is a character string of length eight that consists solely of digits. The last one is a character string consisting solely of alphanumeric characters ('a' to 'z', 'A' to 'Z', and '0' to '9'). Neither whitespaces nor special characters can occur in a message body. You may assume that it is not empty and that its length is at most 50.</p>

<p>You may also assume that there is exactly one space character between any two adjacent fields in an input line representing a rule or a packet.</p>

### 출력 

 <p>For each data set, print the number of legal packets in the first line, followed by all legal packets in the same order as they occur in the data set. Each packet must be written exactly in one line. If the data set includes two packets consisting of the same source and destination addresses and the same message body, you should consider them different packets and so they must be written in different lines. Any extra whitespaces or extra empty lines must not be written.</p>

