# [Bronze II] Maternity - 6860 

[문제 링크](https://www.acmicpc.net/problem/6860) 

### 성능 요약

메모리: 113112 KB, 시간: 120 ms

### 분류

구현

### 문제 설명

<p>Alice and Bob are fruit flies. They are now the proud parents of a new baby girl fly. Unfortunately, due to a slight mix-up, the nurses in the maternity ward at the hospital aren’t sure which baby fly is their daughter. Luckily they’ve hired you to help them out. Using full genetic profiles of the parents, can you figure out which baby fly is theirs?</p>

<p>Recall from biology that attributes (like eye colour, hair colour, etc) are inherited, or passed, from generation to generation. A single gene controls each such attribute. Alternative versions of each gene, called alleles, account for the variation in the attributes. For example, the gene for eye colour exists in two versions, one for brown eyes and one for blue eyes. For each attribute, a fruit fly has two alleles, one inherited from each parent.</p>

<p>If two alleles differ, then one, the dominant allele, will appear in the fruit fly’s appearance. The other, or recessive allele, does not affect the fruit fly’s appearance. Conventionally, the dominant allele is represented by an uppercase letter, and the recessive allele by a lowercase letter. For example, consider the gene for eye colour, B. Each fruit fly has two alleles, each is either that of brown eyes (B, dominant) or blue eyes (b, recessive). If the fruit fly has BB or Bb, she will have brown eyes; if the fruit fly has bb, she will have blue eyes.</p>

<p>When reproducing, each parent fruit fly passes exactly one allele for each gene to its child. We can draw a Punnett square to see all possible allele combinations for the child. For example, here is the Punnett square for possible offspring of Alice (Bb) and Bob (Bb).</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/9854cb1e-92fc-4f7f-80ae-ff120229f5fd/-/preview/" style="width: 160px; height: 88px;"></p>

<p>Unfortunately, the full genetic profiles of the babies were not available (as they take weeks to process). All we have are the attributes of the baby – whether or not they have brown eyes, hair colour, etc. Can you use this information, with the full genetic profile of the parents, to determine which babies could not possibly be theirs?</p>

### 입력 

 <p>Luckily for you, our fruit flies are simple and have exactly five genes, labelled A through E. The input begins with two lines, describing the mother and father, respectively. Each line consists of five pairs of letters, one pair for each gene. Each pair describes the two alleles the parent has for a particular gene. These alleles are listed in order (from A through E).</p>

<p>Next is a line with the number X, X ≤ 10, the number of babies to check. Following are X lines describing the attributes of the baby. Each line consists of five letters in order (from A through E). An uppercase letter denotes the baby shows the attribute of the dominant allele, and a lowercase letter denotes the baby shows the attribute of the recessive allele. For example, if the baby has brown eyes, the letter B will be written; if the baby has blue eyes the letter b will be written.</p>

### 출력 

 <p>For each baby test, output the line “Possible baby.”, if the baby could possibly be their offspring, or “Not their baby!” if impossible.</p>

