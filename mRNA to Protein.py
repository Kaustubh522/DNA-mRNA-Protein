genetic_code = {
    "UUU":"F","UUC":"F","UUA":"L","UUG":"L","CUU":"L","CUC":"L","CUA":"L","CUG":"L",
    "AUU":"I","AUC":"I","AUA":"I","AUG":"M","GUU":"V","GUC":"V","GUA":"V","GUG":"V",
    "UCU":"S","UCC":"S","UCA":"S","UCG":"S","CCU":"P","CCC":"P","CCA":"P","CCG":"P",
    "ACU":"T","ACC":"T","ACA":"T","ACG":"T","GCU":"A","GCC":"A","GCC":"A","GCG":"A",
    "UAU":"Y","UAC":"Y","UAA":"*","UAG":"*","CAU":"H","CAC":"H","CAA":"Q","CAG":"Q",
    "AAU":"N","AAC":"N","AAA":"K","AAG":"K","GAU":"D","GAC":"D","GAA":"E","GAG":"E",
    "UGU":"C","UGC":"C","UGA":"*","UGG":"W","CGU":"R","CGC":"R","CGA":"R","CGG":"R",
    "AGU":"S","AGC":"S","AGA":"R","AGG":"R","GGU":"G","GGC":"G","GGA":"G","GGG":"G"
}

try:
    sequence = input("Enter mRNA sequence:\n").upper()
    sequence = sequence.replace(" ","")
    base=0
    peptide=""
    rem = (len(sequence))%3
    while base<=(len(sequence)-rem-3):
        codon = sequence[base] + sequence[base+1] + sequence[base+2]
        base = base + 3
        peptide += genetic_code.get(codon)
    print("Amino acid sequence of the polypeptide is:\n"+peptide)
    
except:
    print("Invalid Sequence")

