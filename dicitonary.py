d={101:"Ajay",900:"vijay",345:"sanjay",567:"Dharm",678:"vinod"}



print(d)
print(d[567])


print(d.get(567))

print(d.items())

print(d.keys())

print(d.values())
print(d.pop(678))
print(d)

print(d.popitem())
print(d)


d1={567:"karan",678:"mahesh"}
d.update(d1)

print(d)


d[900]="ketan"
print(d)


for i in d:
      print(i," : ",d[i])    
