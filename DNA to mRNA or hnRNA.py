def t2m():
    def t2c(template):
        coding=""
        for base in template:
            if base == "A":
                coding = coding + "U"
            elif base == "T":
                coding = coding + "A"
            elif base == "C":
                coding = coding + "G"
            elif base == "G":
                coding = coding + "C"
            else:
                print("Invalid sequence")
                coding = "NOT DEFINED"
                return coding
        return coding
    print("The mRNA(prokaryotic) or hnRNA(eukaryotic) sequence is:\n"+
          t2c(input("Enter the sequence on template:\n").upper()))

def c2m():
    def t2c(template):
        coding=""
        for base in template:
            if base == "A":
                coding = coding + "A"
            elif base == "T":
                coding = coding + "U"
            elif base == "C":
                coding = coding + "C"
            elif base == "G":
                coding = coding + "G"
            else:
                print("Invalid sequence")
                coding = "NOT DEFINED"
                return coding
        return coding
    print("The mRNA(prokaryotic) or hnRNA(eukaryotic) sequence is:\n"+
          t2c(input("Enter the sequence on coding strand:\n").upper()))

a=input("If you want to enter the sequence on template strand, press 1 and Enter.\nIf you want to enter the sequence on coding strand, press 2 and Enter.\n")
if a=="1":
    t2m()
elif a=="2":
    c2m()
else:
    print("Invalid key")
