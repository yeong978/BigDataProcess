#!/usr/bin/python3
import sys

sum_gen = dict()

in_fp = sys.argv[1]
out_fp = sys.argv[2]

with open(in_fp, "rt") as fp:
    for line in fp:
        str_arr = line.split("::")
        id = int(str_arr[0])
        title = str_arr[1]
        genre = str_arr[2]
        print("ID : %d, Title(year) : %s, Genre : %s" %(id,title,genre), end = '')
        
        gr = genre.split("|")
        last = []
        l = gr.pop()
        last.append(l)
        for s in last:
           arr = s.split()
        arr = arr.pop()
        gr.append(arr)

        for i in gr:        
            if i not in sum_gen:
                sum_gen[i] = 1
            else:
                sum_gen[i] += 1
print(sum_gen)
                 
with open(out_fp, "wt") as fp:
    a = list(sum_gen.keys())
    b = list(sum_gen.values())
    re = zip(a,b)
    result = list(re)
        
    for items in result:
        r = str(items)
        fp.write(r + "\n")
    
                





