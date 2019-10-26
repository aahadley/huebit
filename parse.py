import math
import binascii
f = open("sample.txt","r", encoding="utf-8")
multidarray = []
onedarray = []
if f.mode == 'r':
    f1 = f.readlines()
linenum = 1

for x in f1:

    if "entangled" in x:
        multidarray.append([-1,-1])
        continue
    elif linenum % 3 != 1:
        index1 = x.find("\t") +1
        index2 = x.find("i") + 1
        substring = x[index1:index2]
        splitsubstring = substring.split()
        calc = float(splitsubstring[0]) + float(splitsubstring[2]) *1j
        onedarray.append(calc)
    if linenum %3 == 0:
        onedarray[0],onedarray[1] = onedarray[1],onedarray[0]
        multidarray.append(onedarray)
        onedarray = []
    linenum += 1
print(multidarray)
