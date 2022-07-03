#DNA Template Strand to Coding strand
try:
    def t2c(template):
        coding=""
        for base in template:
            if base not in "AGCT":
                print("Invalid sequence")
                coding="NOT DEFINED"
                return coding
            if base == "A":
                coding = coding + "T"
            elif base == "T":
                coding = coding + "A"
            elif base == "C":
                coding = coding + "G"
            elif base == "G":
                coding = coding + "C"
        return coding
    print("The sequence on the complementary strand is:\n"+
          t2c(input("Enter the sequence on template/coding strand:\n").upper()))
except:
    print("Invalid sequence")

