#!/usr/bin/python3


import datetime
import sys

inp = sys.argv[1]
outp = sys.argv[2]
result = []

with open(inp, "rt") as f:
    for line in f:
        uber_arr = line.split(",")
        base = uber_arr[0]
        date = uber_arr[1]
        vehicle = int(uber_arr[2])
        trip = int(uber_arr[3])
        print("Base number : %s, Date : %s, active vehicles : %d, trips : %d" %(base, date, vehicle, trip))
        
        last = []
        l = uber_arr.pop()
        last.append(l)
        for s in last:
           arr = s.split()
        arr = arr.pop()
        uber_arr.append(arr)
        
        d = uber_arr.pop(1)
        d = d.split("/")
        month = int(d[0])
        day = int(d[1])
        year = int(d[2])
 
        wd = datetime.date(year,month,day).weekday()
        weekday = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
        uber_arr.insert(1,weekday[wd])
        
        for i in uber_arr:
            result.append(i)
print(result)

with open(outp, "wt") as fp:
    for i in result:
        fp.write(i + "\n")




