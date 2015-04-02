def isDNA(seq):
 return seq.count("g")+seq.count("c")+seq.count("a")+seq.count("t")==len(seq)
iets = isDNA("atgagagta")
print(iets)
