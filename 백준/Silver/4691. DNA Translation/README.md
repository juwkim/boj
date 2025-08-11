# [Silver I] DNA Translation - 4691 

[문제 링크](https://www.acmicpc.net/problem/4691) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

브루트포스 알고리즘, 구현, 런타임 전의 전처리, 문자열

### 제출 일자

2025년 8월 12일 00:20:36

### 문제 설명

<p>Deoxyribonucleic acid (DNA) is composed of a sequence of nucleotide bases paired together to form a double-stranded helix structure. Through a series of complex biochemical processes the nucleotide sequences in an organism's DNA are translated into the proteins it requires for life. The object of this problem is to write a computer program which accepts a DNA strand and reports the protein generated, if any, from the DNA strand.</p>

<p>The nucleotide bases from which DNA is built are adenine, cytosine, guanine, and thymine (hereafter referred to as A, C, G, and T, respectively). These bases bond together in a chain to form half of a DNA strand. The other half of the DNA strand is a similar chain, but each nucleotide is replaced by its complementary base. The bases A and T are complementary, as are the bases C and G. These two "half-strands" of DNA are then bonded by the pairing of the complementary bases to form a strand of DNA.</p>

<p>Typically a DNA strand is listed by simply writing down the bases which form the primary strand (the complementary strand can always be created by writing the complements of the bases in the primary strand). For example, the sequence TACTCGTAATTCACT represents a DNA strand whose complement would be ATGAGCATTAAGTGA. Note that A is always paired with T, and C is always paired with G.</p>

<p>From a primary strand of DNA, a strand of ribonucleic acid (RNA) known as messenger RNA (mRNA for short) is produced in a process known as transcription. The transcribed mRNA is identical to the complementary DNA strand with the exception that thymine is replaced by a nucleotide known as uracil (hereafter referred to as U). For example, the mRNA strand for the DNA in the previous paragraph would be AUGAGCAUUAAGUGA.</p>

<p>It is the sequence of bases in the mRNA which determines the protein that will be synthesized. The bases in the mRNA can be viewed as a collection of codons, each codon having exactly three bases. The codon AUG marks the start of a protein sequence, and any of the codons UAA, UAG, or UGA marks the end of the sequence. The one or more codons between the start and termination codons represent the sequence of amino acids to be synthesized to form a protein. For example, the mRNA codon AGC corresponds to the amino acid serine (Ser), AUU corresponds to isoleucine (Ile), and AAG corresponds to lysine (Lys). So, the protein formed from the example mRNA in the previous paragraph is, in its abbreviated form, Ser-Ile-Lys.</p>

<p>The complete genetic code from which codons are translated into amino acids is shown in the table below (note that only the amino acid abbreviations are shown). It should also be noted that the sequence AUG, which has already been identified as the start sequence, can also correspond to the amino acid methionine (Met). So, the first AUG in a mRNA strand is the start sequence, but subsequent AUG codons are translated normally into the Met amino acid.</p>

<table class="table table-bordered" style="width:40%">
	<thead>
		<tr>
			<th rowspan="2">First base in codon</th>
			<th colspan="4">Second base in codon</th>
			<th rowspan="2">Third base in codon</th>
		</tr>
		<tr>
			<th>U</th>
			<th>C</th>
			<th>A</th>
			<th>G</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th rowspan="4">U</th>
			<td>Phe</td>
			<td>Ser</td>
			<td>Tyr</td>
			<td>Cys</td>
			<th>U</th>
		</tr>
		<tr>
			<td>Phe</td>
			<td>Ser</td>
			<td>Tyr</td>
			<td>Cys</td>
			<th>C</th>
		</tr>
		<tr>
			<td>Leu</td>
			<td>Ser</td>
			<td>---</td>
			<td>---</td>
			<th>A</th>
		</tr>
		<tr>
			<td>Leu</td>
			<td>Ser</td>
			<td>---</td>
			<td>Trp</td>
			<th>G</th>
		</tr>
		<tr>
			<th rowspan="4">C</th>
			<td>Leu</td>
			<td>Pro</td>
			<td>His</td>
			<td>Arg</td>
			<th>U</th>
		</tr>
		<tr>
			<td>Leu</td>
			<td>Pro</td>
			<td>His</td>
			<td>Arg</td>
			<th>C</th>
		</tr>
		<tr>
			<td>Leu</td>
			<td>Pro</td>
			<td>Gln</td>
			<td>Arg</td>
			<th>A</th>
		</tr>
		<tr>
			<td>Leu</td>
			<td>Pro</td>
			<td>Gln</td>
			<td>Arg</td>
			<th>G</th>
		</tr>
		<tr>
			<th rowspan="4">A</th>
			<td>Ile</td>
			<td>Thr</td>
			<td>Asn</td>
			<td>Ser</td>
			<th>U</th>
		</tr>
		<tr>
			<td>Ile</td>
			<td>Thr</td>
			<td>Asn</td>
			<td>Ser</td>
			<th>C</th>
		</tr>
		<tr>
			<td>Ile</td>
			<td>Thr</td>
			<td>Lys</td>
			<td>Arg</td>
			<th>A</th>
		</tr>
		<tr>
			<td>Met</td>
			<td>Thr</td>
			<td>Lys</td>
			<td>Arg</td>
			<th>G</th>
		</tr>
		<tr>
			<th rowspan="4">G</th>
			<td>Val</td>
			<td>Ala</td>
			<td>Asp</td>
			<td>Gly</td>
			<th>U</th>
		</tr>
		<tr>
			<td>Val</td>
			<td>Ala</td>
			<td>Asp</td>
			<td>Gly</td>
			<th>C</th>
		</tr>
		<tr>
			<td>Val</td>
			<td>Ala</td>
			<td>Glu</td>
			<td>Gly</td>
			<th>A</th>
		</tr>
		<tr>
			<td>Val</td>
			<td>Ala</td>
			<td>Glu</td>
			<td>Gly</td>
			<th>G</th>
		</tr>
		<tr>
		</tr>
	</tbody>
</table>

### 입력 

 <p>The input for this program consists of strands of DNA sequences, one strand per line, from which the protein it generates, if any, should be determined and output. The given DNA strand may be either the primary or the complementary DNA strand, and it may appear in either forward or reverse order, and the start and termination sequences do not necessarily appear at the ends of the strand. For example, a given input DNA strand to form the protein Ser-Ile-Lys could be any of ATACTCGTAATTCACTCC, CCTCACTTAATGCTCATA, TATGAGCATTAAGTGAGG, or GGAGTGAATTACGAGTAT. The input file will be terminated by a line containing a single asterisk character.</p>

### 출력 

 <p>You may assume the input to contain only valid, upper-case, DNA nucleotide base letters (A, C, G, and T). No input line will exceed 255 characters in length. There will be no blank lines or spaces in the input. Some sequences, though valid DNA strands, do not produce valid protein sequences; the string "*** No translatable DNA found ***" should be output when an input DNA strand does not translate into a valid protein.</p>

