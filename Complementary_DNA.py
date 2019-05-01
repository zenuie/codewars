def DNA_strand(dna):
    # code here
    total = []
    newtotal = ""
    for i in dna:
        if i == "A":
            total.append("T")
        elif i == "T":
            total.append("A")
        elif i == "C":
            total.append("G")
        elif i == "G":
            total.append("C")
    for i in total:
        newtotal+=i
    return newtotal