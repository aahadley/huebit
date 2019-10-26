import math
import binascii
f = open("sample.txt","r", encoding="utf-8")
arrays = []
tempar = []
if f.mode == 'r':
    f1 = f.readlines()
linenum = 1

for x in f1:

    if "entangled" in x:
        arrays.append([-1,-1])
        continue
    elif linenum % 3 != 1:
        index1 = x.find("\t") +2
        index2 = x.find("i") + 1
        sub = x[index1:index2]
        brokesub = sub.split()
        mynum = float(brokesub[0]) + float(brokesub[2])
        tempar.append(mynum)
    if linenum %3 == 0:
        print(tempar)
        arrays.append(tempar)
        tempar = []
    linenum += 1
print(arrays)
